from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime


class SaddleAssignWizard(models.TransientModel):
    _name = 'saddle.assign.wizard'

    saddle_id = fields.Many2one('saddle.data', string='Saddle')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')

    def assign(self):
        if self.saddle_id:
            partner_record = self.env['res.partner'].browse(self.env.context.get('active_id'))
            partner_record.write({
                'saddle_assigned': self.saddle_id.id
            })

            self.env['horse.assign.data'].create({
                'partner_id': partner_record.id,
                'saddle_id': self.saddle_id.id,
                'start_date': self.start_date,
                'end_date': self.end_date,
            })