from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class HorseAssignData(models.Model):
    _name = 'horse.assign.data'
    _description = "Horse Assign Database"

    partner_id = fields.Many2one('res.partner', string='Partner', tracking=True)
    horse_id = fields.Many2one('horse.data', string='Horse', tracking=True)
    start_date = fields.Datetime(string='Start Date', tracking=True)
    end_date = fields.Datetime(string='End Date', tracking=True)