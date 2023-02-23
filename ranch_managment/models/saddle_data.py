from odoo import models, fields, api, _


class SaddleData(models.Model):
    _name = 'saddle.data'
    _description = "saddle Database"

    rack_number = fields.Char()
    maker = fields.Char()
    purchase_date = fields.Date()
    seat_size = fields.Integer()
    stirrup_max = fields.Integer()
    stirrup_min = fields.Integer()
    saddle_serial = fields.Integer()
    in_use = fields.Boolean()
