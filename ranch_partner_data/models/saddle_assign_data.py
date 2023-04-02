from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class SaddleAssignData(models.Model):
    _name = 'saddle.assign.data'
    _description = "saddle Assign Database"

    partner_id = fields.Many2one('res.partner', string='Partner', tracking=True)
    horse_id = fields.Many2one('saddle.data', string='saddle', tracking=True)
    start_date = fields.Datetime(string='Start Date', tracking=True)
    end_date = fields.Datetime(string='End Date', tracking=True)