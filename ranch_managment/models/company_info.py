from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    first_guest_week = fields.Yearweek()
    last_guet_week = fields.Yearweek()
