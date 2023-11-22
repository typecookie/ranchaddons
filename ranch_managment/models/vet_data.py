from odoo import models, fields, api, _


class VetData(models.Model):
    _name = 'vet.data'
    _description = "vet Database"

    horse_id = fields.Many2one('horse.data', string='Horse', tracking=True)
    Diagnosis = fields.Char(tracking=True)
    Treatment = fields.Char(tracking=True)
    Notes = fields.Char(tracking=True)
    Vet_Begin_date = fields.Date(tracking=True)
    Vet_End_date = fields.Date(tracking=True)
