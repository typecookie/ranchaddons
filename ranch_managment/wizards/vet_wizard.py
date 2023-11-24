from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime


class VetWizard(models.TransientModel):
    _name = 'vet.wizard'

    horse_id = fields.Many2one('horse.data', string='Horse')
    Vet_Begin_date = fields.Datetime(string='Start Date')
    Vet_End_date = fields.Datetime(string='End Date')
    Diagnosis = fields.Char(string="Diagnosis")
    Treatment = fields.Char(string="Treatment")
    Notes = fields.Char(string="Notes")

    def assign(self):
        if self.horse_id:
            partner_record = self.env['horse.data'].browse(self.env.context.get('active_id'))
            partner_record.write({
                'vet_data_ids': self.horse_id.id
            })

            self.env['vet.data'].create({
                'name': self.horse_id.id,
                'Vet_Begin_date': self.Vet_Begin_date,
                'Vet_End_date': self.Vet_End_date,
                'Diagnosis': self.Diagnosis,
                'Treatment': self.Treatment,
                'Notes': self.Notes

            })
