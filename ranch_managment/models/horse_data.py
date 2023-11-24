from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class HorseData(models.Model):
    _name = 'horse.data'
    _description = "Horse Database"
    # _inherit = 'image.mixin'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', required=True, tracking=True)
    horse_birth_date = fields.Date("Birthdate", tracking=True)
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
    tag_ids = fields.Many2many('horse.data.tag', string='Tags')
    vet_data_ids = fields.One2many('vet.data', 'name', string='vet_name')
    horse_vitals_ids = fields.One2many('horse.vitals', 'name', string='vet_name')

    @api.depends("horse_birth_date")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.horse_birth_date:
                age = relativedelta(fields.Date.today(), record.horse_birth_date).years
            record.age = age


class HorseDataTag(models.Model):
    _name = 'horse.data.tag'
    _description = "Horse Database Tag"

    name = fields.Char('Name', required=True, tracking=True)
