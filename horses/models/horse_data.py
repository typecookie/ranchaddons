from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class HorseData(models.Model):
    _name = 'horses.data'
    name = fields.Char('Name', required=True)
    birth_date = fields.Date("Birthdate")
    age = fields.Integer(string="Age", readonly=True, compute="_compute_age")
    advanced = fields.Boolean()
    beginner = fields.Boolean()
    intermediate = fields.Boolean()

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.birthdate_date:
                age = relativedelta(fields.Date.today(), record.birthdate_date).years
            record.age = age
