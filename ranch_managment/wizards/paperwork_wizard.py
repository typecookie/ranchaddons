from odoo import models, fields, api


class ReservationWizard(models.TransientModel):
    _name = "reservation.wizard"
    _description = "Reservation Query Wizard"

    # Step 1: Date Range Input
    check_in_date = fields.Date(string="Check-In Date", required=True)
    check_out_date = fields.Date(string="Check-Out Date", required=True)

    # Step 2: Query Options
    query_option = fields.Selection([
        ('paperwork', 'Paperwork'),
        ('barn', 'Barn'),
        ('handout', 'Handout'),
    ], string="Query Option", required=True, default='paperwork')

    @api.model
    def _get_filtered_reservations(self):
        """Helper method to filter reservations based on check-in and check-out dates."""
        return self.env['reservation.reservation'].search([
            ('check_in', '>=', self.check_in_date),
            ('check_out', '<=', self.check_out_date),
        ])

    def action_query_reservations(self):
        """
        Executes the relevant query based on the selected option, then opens a view.
        """
        # Filter reservations based on date range
        reservations = self._get_filtered_reservations()

        # Route the query based on the selected query_option
        if self.query_option == 'paperwork':
            return self._action_paperwork(reservations)
        elif self.query_option == 'barn':
            return self._action_barn(reservations)
        elif self.query_option == 'handout':
            return self._action_handout(reservations)

    def _action_paperwork(self, reservations):
        """Option 1: Paperwork"""
        member_data = self.env['reservation.member'].search([
            ('reservation_id', 'in', reservations.ids)
        ])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Paperwork',
            'res_model': 'reservation.member',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', member_data.ids)],
        }

    def _action_barn(self, reservations):
        """Option 2: Barn (Horse/Saddle Data with Additional Fields)"""
        member_data = self.env['reservation.member'].search([
            ('reservation_id', 'in', reservations.ids)
        ])
        family_member_data = self.env['family.member.data'].search([])  # Example, adjust as needed
        return {
            'type': 'ir.actions.act_window',
            'name': 'Barn Data',
            'res_model': 'reservation.member',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', member_data.ids)],
        }

    def _action_handout(self, reservations):
        """Option 3: Handout (Family Data such as Allergies and Dietary Needs)"""
        family_data = self.env['guest.family.data'].search([])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Handout Data',
            'res_model': 'guest.family.data',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', family_data.ids)],
        }
