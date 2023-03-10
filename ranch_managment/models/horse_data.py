from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class HorseData(models.Model):
    _name = 'horse.data'
    _description = "Horse Database"
    _inherit = 'image.mixin'

    name = fields.Char('Name', required=True)
    horse_birth_date = fields.Date("Birthdate")
    age = fields.Integer(string="Age", readonly=True, compute="_compute_age")
    advanced = fields.Boolean()
    beginner = fields.Boolean()
    intermediate = fields.Boolean()
    brands = fields.Char()
    details = fields.Char()
    purchase_date = fields.Date()
    guest_use = fields.Boolean()
    wrangler_use = fields.Boolean()
    bridle_data = fields.Char()

    @api.depends("horse_birth_date")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.horse_birth_date:
                age = relativedelta(fields.Date.today(), record.horse_birth_date).years
            record.age = age
