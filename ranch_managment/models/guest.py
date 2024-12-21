from PIL.features import features

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class GuestFamilyData(models.Model):
    _name = 'guest.family.data'
    _description = "Family Database"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _rec_name = 'lastname'
    member_ids = fields.One2many('family.member.data', 'family_id', string='Members')

    lastname = fields.Char('Last Name', required=True, tracking=True)
    firstname = fields.Char('First Name', required=True, tracking=True)
    number_of_years_return = fields.Integer()
    cabin_owner = fields.Boolean()
    cabin_preference = fields.Char()
    anniversaries = fields.Text()
    birthdays = fields.Text()
    streetline1 = fields.Char()
    streetline2 = fields.Char()
    city = fields.Char()
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', string='State')
    zip = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    fax = fields.Char()
    website = fields.Char()
    tag_ids = fields.Many2many('family.data.tag', string='Tags')
    reservation_ids = fields.Many2many('reservation.reservation', 'reservation_family_rel', 'family_id',
                                       'reservation_id',
                                       string='Reservations')
class FamilyDataTag(models.Model):
    _name = 'family.data.tag'
    _description = "Family Tag table"
    _rec_name = 'name'  # Specify the field used for the display name

    name = fields.Char('Name', required=True, tracking=True)  # Ensure field definition is complete

class FamilyMembersData(models.Model):
    _name = 'family.member.data'
    _description = "Family member Database"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _rec_name = 'firstname'

    family_id = fields.Many2one('guest.family.data', string='Family', required=True)
    lastname = fields.Char('Last Name', required=True, tracking=True)
    firstname = fields.Char('First Name', required=True, tracking=True)
    height = fields.Float()
    weight = fields.Integer()
    exp = fields.Char()
    sex = fields.Char()
    birthdate = fields.Date("Birthdate")
    age = fields.Integer(string="Age", readonly=True, compute="_compute_age")
    food_allergies = fields.Text()
    dietary_needs = fields.Text()
    health_conditions = fields.Text()
    health_requests = fields.Text()
    horse_request = fields.Char()
    saddle_request = fields.Integer()
    is_coming = fields.Boolean(default=True)
    
    @api.depends("birthdate")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.birthdate:
                age = relativedelta(fields.Date.today(), record.birthdate).years
            record.age = age


