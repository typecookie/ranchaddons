from odoo import api, exceptions, fields, models
from dateutil.relativedelta import relativedelta

class Reservation(models.Model):
    _name = 'reservation.reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Reservation"
    _rec_name = 'reservation_dates'  # set _rec_name to 'reservation_dates'
    family_ids = fields.Many2many("guest.family.data", "reservation_family_rel", "reservation_id", "family_id",
                                  string='Reservations')
    reservation_dates = fields.Char(compute='_compute_reservation_dates', readonly=True, store=True)
    check_in = fields.Datetime(required=True)
    check_out = fields.Datetime(required=True)
    room_ids = fields.Many2many('cabins.data', string='Cabins')
    adults = fields.Integer()
    kids = fields.Integer()
    notes = fields.Text()
    deposit_request_sent = fields.Boolean()
    deposit_request_received = fields.Boolean()
    deposit_request_received_date = fields.Date()
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='draft')

    @api.depends('check_in', 'check_out')
    def _compute_reservation_dates(self):
        for rec in self:
            rec.reservation_dates = f"Check In: {rec.check_in}, Check Out: {rec.check_out}"

    @api.model
    def create(self, vals):
        reservation = super().create(vals)

        for family in reservation.family_ids:
            for member in family.member_ids:
                # Create a record for each family member in reservation.member model
                self.env['reservation.member'].create({
                    'reservation_id': reservation.id,
                    'member_id': member.id,
                })

    def write(self, vals):
        # Update the Reservation first
        reservation_updated = super().write(vals)

        for family in self.family_ids:
            for member in family.member_ids:
                existing = self.env['reservation.member'].search(
                    [('member_id', '=', member.id), ('reservation_id', '=', self.id)])
                if not existing:
                    self.env['reservation.member'].create({
                        'member_id': member.id,
                        'reservation_id': self.id,
                    })

        return reservation_updated

class ReservationMember(models.Model):
    _name = 'reservation.member'
    _description = "Reservation Member"
    _rec_name = 'reservation_dates'  # set _rec_name to 'reservation_dates'
    reservation_id = fields.Many2one('reservation.reservation', string='Reservation', ondelete='cascade')
    reservation_dates = fields.Char(related='reservation_id.reservation_dates', readonly=True)
    member_id = fields.Many2one('family.member.data', string='Family Member',
                                domain=[('is_coming', '=', True)],
                                ondelete='cascade')
    check_in = fields.Datetime(related='reservation_id.check_in', readonly=True)
    check_out = fields.Datetime(related='reservation_id.check_out', readonly=True)

    release_form_signed = fields.Boolean(string="Release Form Signed")
    assigned_saddle = fields.Many2one('saddle.data', string="Assigned Saddle")
    assigned_horse = fields.Many2one('horse.data', string="Assigned Horse")