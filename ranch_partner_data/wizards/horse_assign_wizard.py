from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime


class HorseAssignWizard(models.TransientModel):
    _name = 'horse.assign.wizard'

    horse_id = fields.Many2one('horse.data', string='Horse')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')

    def assign(self):
        if self.horse_id:
            partner_record = self.env['res.partner'].browse(self.env.context.get('active_id'))
            partner_record.write({
                'horse_assigned': self.horse_id.id
            })

            self.env['horse.assign.data'].create({
                'partner_id': partner_record.id,
                'horse_id': self.horse_id.id,
                'start_date': self.start_date,
                'end_date': self.end_date,
            })