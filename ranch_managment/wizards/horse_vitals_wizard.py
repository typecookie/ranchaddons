from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime

class HorseVitalsWizard(models.TransientModel):
    _name = 'horse.vitals.wizard'

    horse_id = fields.Many2one('horse.data', string='Horse')
    Temp = fields.Char(string='Temp')
    BPM = fields.Char(string='BPM')
    Notes = fields.Char(string="Notes")

    def assign(self):
        if self.horse_id:
            partner_record = self.env['horse.data'].browse(self.env.context.get('active_id'))
            partner_record.write({
                'horse_vitals_ids': self.horse_id.id
            })

            self.env['horse.vitals'].create({
                'name': self.horse_id.id,
                'Temp': self.Temp,
                'BPM': self.BPM,
                'Notes': self.Notes

            })
