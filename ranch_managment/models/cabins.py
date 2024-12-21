from odoo import models, fields


class Cabins(models.Model):
    _name = 'cabins.data'
    _description = "Cabin Database"

    cabin_name_number = fields.Char()
    cabin_min = fields.Integer()
    cabin_max = fields.Integer()
    cabin_maintanice_ids = fields.One2many('cabins.maintaince', 'cabin_id')
    canin_inventory_ids = fields.One2many('cabins.inventory', 'cabin_id')


class CabinMaintaince(models.Model):
    _name = 'cabins.maintaince'
    _description = "Cabin Maintaince Database"

    cabin_id = fields.Many2one('cabins.data', ondelete='cascade')
    description = fields.Char()
    request = fields.Boolean()
    request_date = fields.Datetime()
    complete_date = fields.Datetime()
    notes = fields.Text()
    total_cost = fields.Float()


class CabinInventory(models.Model):
    _name = 'cabins.inventory'
    _description = "Cabin Inventory Database"

    cabin_id = fields.Many2one('cabins.data', ondelete='cascade')
    common_name = fields.Char()
    part_number = fields.Char()
    item_id = fields.Many2one('cabins.inventory.item', string='Item')
    quantity = fields.Integer()
    unit_price = fields.Float()
    total_price = fields.Float()
