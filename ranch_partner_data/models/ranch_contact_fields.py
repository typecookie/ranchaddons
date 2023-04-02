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
    food_allergies = fields.Text()
    dietary_needs = fields.Text()
    health_conditions = fields.Text()
    health_requests = fields.Text()
    number_of_years_return = fields.Integer()
    horse_request = fields.Char()
    horse_assigned = fields.Many2one('horse.data', string='Horse')
    cabin_owner = fields.Boolean()
    cabin_preference = fields.Char()
    deposit_request_sent = fields.Boolean()
    deposit_request_received = fields.Boolean()
    deposit_request_received_date = fields.Date()
    saddle_request = fields.Integer()
    saddle_assigned = fields.Integer()
    anniversaries = fields.Text()
    birthdays = fields.Text()

    reservation_ids = fields.One2many('hotel.reservation', 'partner_id', string='Reservations')
    horse_assign_ids = fields.One2many('horse.assign.data', 'partner_id', string='Horses Assign')

    @api.depends("birthdate_date")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.birthdate_date:
                age = relativedelta(fields.Date.today(), record.birthdate_date).years
            record.age = age
