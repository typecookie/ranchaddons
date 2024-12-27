
from odoo import models, fields, api, _  # Ensure there’s no duplicate import here
from datetime import datetime


class YearlyRanchData(models.Model):
    _name = 'yearly.ranch.data'
    _description = 'Ranch Data By Year'
    _sql_constraints = [
        ('unique_year', 'unique(year)', 'There can only be one record per year.')
    ]

    year = fields.Integer(required=True)
    first_guest_week = fields.Date()
    last_guest_week = fields.Date()
    check_in_time = fields.Float()
    check_out_time = fields.Float()

    def get_checkin_datetime(self, checkin_date):
        return datetime.combine(checkin_date, datetime.min.time()) + timedelta(hours=self.check_in_time)

    def get_checkout_datetime(self, checkout_date):
        return datetime.combine(checkout_date, datetime.min.time()) + timedelta(hours=self.check_out_time)