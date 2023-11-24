from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime


class VetWizard(models.TransientModel):
    _name = 'vet.wizard'

    horse_id = fields.Many2one('horse.data', string='Horse')
    Vet_Start_date = fields.Datetime(string='Start Date')
    Vet_End_date = fields.Datetime(string='End Date')
    Diagnosis = fields.Char(string="Diagnosis")
    Treatment = fields.Char(string="Treatment")
    Notes = fields.Char(string="Notes")

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