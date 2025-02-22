from odoo import api, exceptions, fields, models
from dateutil.relativedelta import relativedelta


class Reservation(models.Model):
    _name = 'reservation.reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Reservation"
    _rec_name = 'check_in'
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
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
                             default='draft')
    is_driving = fields.Boolean(string="Driving?")
    flight_number = fields.Char()
    airport = fields.Char()
    arrival_time = fields.Datetime()
    departure_time = fields.Datetime()


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
        return reservation

    def write(self, vals):
        # Update the Reservation first
        reservation_updated = super().write(vals)

        if reservation_updated:
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
    _rec_name = 'check_in_str'

    reservation_id = fields.Many2one('reservation.reservation', string='Reservation', ondelete='cascade')
    check_in_str = fields.Char(compute='_compute_check_in_str', readonly=True, store=True)
    member_id = fields.Many2one('family.member.data', string='Family Member',
                                domain=[('is_coming', '=', True)],
                                ondelete='cascade')
    check_in = fields.Datetime(related='reservation_id.check_in', readonly=True)
    check_out = fields.Datetime(related='reservation_id.check_out', readonly=True)

    release_form_signed = fields.Boolean(string="Release Form Signed", default=False)
    assigned_saddle = fields.Many2one('saddle.data', string="Assigned Saddle", default=False)
    assigned_horse = fields.Many2one('horse.data', string="Assigned Horse", default=False)

    @api.depends('reservation_id.check_in', 'check_in', 'check_out')
    def _compute_reservation_dates(self):
        pass

    @api.depends('check_in')
    def _compute_check_in_str(self):
        for rec in self:
            rec.check_in_str = rec.check_in.strftime("%Y-%m-%d %H:%M:%S") if rec.check_in else ''

    @api.model
    def create(self, vals):
        res = super(ReservationMember, self).create(vals)
        return res

    def write(self, vals):
        res = super(ReservationMember, self).write(vals)
        return res

    @api.onchange('reservation_id')
    def _onchange_reservation_id(self):
        """Populate related fields when reservation_id is set or changed."""
        if self.reservation_id:
            # Example: Populate `member_id` dynamically based on the reservation
            self.member_id = self.reservation_id.member_id.id or False

            # If you have other linked fields to populate, include them here
            self.release_form_signed = self.reservation_id.release_form_signed
            self.assigned_saddle = self.reservation_id.default_saddle_id
            self.assigned_horse = self.reservation_id.default_horse_id
