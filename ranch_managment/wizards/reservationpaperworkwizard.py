from odoo import api, exceptions, fields, models
from odoo.exceptions import ValidationError

class ReservationMemberWizard(models.TransientModel):
    _name = 'reservation.member.wizard'
    _description = 'Reservation Member Wizard'

    start_date = fields.Date('Start Check-in Date', required=True)
    end_date = fields.Date('End Check-in Date', required=True)

    def action_show_members(self):
        member_ids = self.env['reservation.member'].search([
            ('reservation_id.check_in', '>=', self.start_date),
            ('reservation_id.check_in', '<=', self.end_date),
            ('release_form_signed', '=', False)
        ]).mapped('member_id').ids

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'family.member.data',
            'domain': [('id', 'in', member_ids)],
        }