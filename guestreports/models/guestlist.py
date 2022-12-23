from odoo import api, exceptions, fields, models, _


class DataFromBooking(models.Model):
    _name = "guestlistcomp"
    _description = "List guest by week"

    company_name_from_res = fields.selection('res.partner.company_id', string='company',readonly=True)
#    partner_id = fields.Selection(
#       "res.partner",
#        "Guest Name",
#        readonly=True,
#        index=True,
#        required=True,
#        states={"draft": [("readonly", True)]},
#    )
#
#    checkin = fields.Selection(related=hotel.checkin
#        "Expected-Date-Arrival",
#        required=True,
#        readonly=True,
#        states={"draft": [("readonly", True)]},
#    )
#    checkout = fields.Selection(
#        "Expected-Date-Departure",
#        required=True,
#        readonly=True,
#        states={"draft": [("readonly", True)]},
#    )
