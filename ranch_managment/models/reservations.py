from odoo import api, exceptions, fields, models
from dateutil.relativedelta import relativedelta

class Reservation(models.Model):
    _name = 'reservation.reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Reservation"

    family_ids = fields.Many2many("guest.family.data", "reservation_family_rel", "reservation_id", "family_id",
                                  string='Reservations')
    check_in = fields.Datetime(required=True)
    check_out = fields.Datetime(required=True)
    room_ids = fields.Many2many('cabins.data', string='Cabins')
    adults = fields.Integer(required=True)
    kids = fields.Integer(required=True)
    notes = fields.Text()
    deposit_request_sent = fields.Boolean()
    deposit_request_received = fields.Boolean()
    deposit_request_received_date = fields.Date()
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='draft')