from odoo import api, exceptions, fields, models, _


class DataFromBooking(models.Model):
    _name = "BookingToGuestList"
    _description = "List guest by week"
    _inherit = 'hotel.reservation'

    booking_data = fields.Many2many('hotel.reservation', string='checkin')
