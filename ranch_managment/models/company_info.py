from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    first_guest_week = fields.Date()
    last_guet_week = fields.Date()
    checkin_time = fields.Text()
    checkout_time = fields.Text()
