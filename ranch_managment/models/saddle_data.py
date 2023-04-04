from odoo import models, fields, api, _


class SaddleData(models.Model):
    _name = 'saddle.data'
    _description = "saddle Database"

    rack_number = fields.Char()
    maker = fields.Char()
    purchase_date = fields.Date()
    seat_size = fields.Float(digits=(12,1))
    stirrup_max = fields.Float(digits=(12,2))
    stirrup_min = fields.Float(digits=(12,2))
    saddle_serial = fields.Integer()
    in_use = fields.Boolean()
