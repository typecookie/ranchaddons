from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
import random


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def get_random_color(self):
        colors = ['red', 'blue', 'green', 'yellow', 'gold']
        color = random.choice(colors)
        return color