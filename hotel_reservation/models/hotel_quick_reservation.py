# See LICENSE file for full copyright and licensing details.

import logging
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

_logger = logging.getLogger(__name__)
try:
    import pytz
except (ImportError, IOError) as err:
    _logger.debug(err)


class QuickRoomReservation(models.TransientModel):
    _name = "quick.room.reservation"
    _description = "Quick Room Reservation"

    partner_id = fields.Many2one("res.partner", "Customer", required=True)
    check_in = fields.Datetime("Check In", required=True)
    check_out = fields.Datetime("Check Out", required=True)
    room_id = fields.Many2one("hotel.room", "Room", required=True)
    company_id = fields.Many2one("res.company", "Hotel", required=True)
    pricelist_id = fields.Many2one("product.pricelist", "pricelist")
    partner_invoice_id = fields.Many2one(
        "res.partner", "Invoice Address", required=True
    )
    partner_order_id = fields.Many2one("res.partner", "Ordering Contact", required=True)
    partner_shipping_id = fields.Many2one(
        "res.partner", "Delivery Address", required=True
    )
    adults = fields.Integer("Adults")

    @api.onchange("check_out", "check_in")
    def _on_change_check_out(self):
        """
        When you change checkout or checkin it will check whether
        Checkout date should be greater than Checkin date
        and update dummy field
        -----------------------------------------------------------
        @param self: object pointer
        @return: raise warning depending on the validation
        """
        if (self.check_out and self.check_in) and (self.check_out < self.check_in):
            raise ValidationError(
                _("Checkout date should be greater than Checkin date.")
            )

    @api.onchange("partner_id")
    def _onchange_partner_id_res(self):
        """
        When you change partner_id it will update the partner_invoice_id,
        partner_shipping_id and pricelist_id of the hotel reservation as well
        ---------------------------------------------------------------------
        @param self: object pointer
        """
        if not self.partner_id:
            self.update(
                {
                    "partner_invoice_id": False,
                    "partner_shipping_id": False,
                    "partner_order_id": False,
                }
            )
        else:
            addr = self.partner_id.address_get(["delivery", "invoice", "contact"])
            self.update(
                {
                    "partner_invoice_id": addr["invoice"],
                    "partner_shipping_id": addr["delivery"],
                    "partner_order_id": addr["contact"],
                    "pricelist_id": self.partner_id.property_product_pricelist.id,
                }
            )

    @api.model
    def default_get(self, fields):
        """
        To get default values for the object.
        @param self: The object pointer.
        @param fields: List of fields for which we want default values
        @return: A dictionary which of fields with values.
        """
        res = super(QuickRoomReservation, self).default_get(fields)
        keys = self._context.keys()

        if "date" in keys:
            # res.update({"check_in": self._context["date"]})

            timezone = pytz.timezone(self._context.get('tz') or 'UTC')

            free_date = datetime.strptime(self._context["date"], '%Y-%m-%d %H:%M:%S')
            free_date = free_date.replace(tzinfo=pytz.timezone("UTC")).astimezone(timezone)

            # get default checkin time from company
            if self.env.company.checkin_time:
                default_checkin = str(free_date.date()) + ' ' + self.env.company.checkin_time + ':00'
            else:
                default_checkin = str(free_date.date()) + ' ' + '00:00:00'

            # get default checkout time from company
            if self.env.company.checkout_time:
                default_checkout = str(free_date.date() + timedelta(days=1)) + ' ' + self.env.company.checkout_time + ':00'
            else:
                default_checkout = str(free_date.date() + timedelta(days=1)) + ' ' + '00:00:00'

            d_checkin_obj = timezone.localize(datetime.strptime(default_checkin, '%Y-%m-%d %H:%M:%S'), is_dst=None).astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')
            d_checkout_obj = timezone.localize(datetime.strptime(default_checkout, '%Y-%m-%d %H:%M:%S'), is_dst=None).astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')

            res.update({"check_in": d_checkin_obj})
            res.update({"check_out": d_checkout_obj})

        if "room_id" in keys:
            roomid = self._context["room_id"]
            res.update({"room_id": int(roomid)})
        return res

    def room_reserve(self):
        """
        This method create a new record for hotel.reservation
        -----------------------------------------------------
        @param self: The object pointer
        @return: new record set for hotel reservation.
        """
        hotel_res_obj = self.env["hotel.reservation"]
        for res in self:
            rec = hotel_res_obj.create(
                {
                    "partner_id": res.partner_id.id,
                    "partner_invoice_id": res.partner_invoice_id.id,
                    "partner_order_id": res.partner_order_id.id,
                    "partner_shipping_id": res.partner_shipping_id.id,
                    "checkin": res.check_in,
                    "checkout": res.check_out,
                    "company_id": res.company_id.id,
                    "pricelist_id": res.pricelist_id.id,
                    "adults": res.adults,
                    "reservation_line": [
                        (
                            0,
                            0,
                            {
                                "reserve": [(6, 0, res.room_id.ids)],
                                "name": res.room_id.name or " ",
                            },
                        )
                    ],
                }
            )
        return rec
