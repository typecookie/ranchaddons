from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime


class HorseAssignUpdateWizard(models.TransientModel):
    _name = 'saddle.assign.update.wizard'

    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')

    @api.model
    def default_get(self, fields):
        result = super(SaddleAssignUpdateWizard, self).default_get(fields)
        horse_assign_record = self.env['saddle.assign.data'].browse(self.env.context.get('active_id'))
        result['start_date'] = saddle_assign_record.start_date
        result['end_date'] = saddle_assign_record.end_date
        return result

    def update(self):
        if self.start_date or self.end_date:
            saddle_assign_record = self.env['saddle.assign.data'].browse(self.env.context.get('active_id'))
            saddle_assign_record.write({
                'start_date': self.start_date if self.start_date else saddle_assign_record.start_date,
                'end_date': self.end_date if self.end_date else saddle_assign_record.end_date,
            })