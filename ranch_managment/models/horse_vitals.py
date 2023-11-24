from odoo import models, fields, api, _


class HorseVitals(models.Model):
    _name = 'horse.vitals'
    _description = "Vitals DB"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(tracking=True)
    Temp = fields.Char(tracking=True)
    BPM = fields.Char(tracking=True)
    Notes = fields.Char(tracking=True)
