# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models, _
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = 'res.partner'
    Height = fields.Float()
    Weight = fields.Integer()
    Exp = fields.Char()
    Sex = fields.Char()
    birthdate_date = fields.Date("Birthdate")
    age = fields.Integer(string="Age", readonly=True, compute="_compute_age")

    @api.depends("birthdate_date")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.birthdate_date:
                age = relativedelta(fields.Date.today(), record.birthdate_date).years
            record.age = age