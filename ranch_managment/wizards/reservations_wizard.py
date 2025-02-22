from odoo import models, fields


class ReservationWizard(models.TransientModel):
    _name = 'reservation.wizard'

    check_in = fields.Datetime(required=True)
    check_out = fields.Datetime(required=True)
    room_ids = fields.Many2many('cabins.data', string='Cabins')

    def confirm(self):
        # Use self.env.context to get the active family id
        family_id = self.env.context.get('active_id')
        family = self.env['guest.family.data'].browse(family_id)

        new_reservation = self.env['reservation.reservation'].create({
            'family_ids': [(6, 0, family.ids)],
            'check_in': self.check_in,
            'check_out': self.check_out,
            'room_ids': self.room_ids.ids
        })
