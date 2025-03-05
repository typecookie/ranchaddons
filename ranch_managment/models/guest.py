from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class GuestFamilyData(models.Model):
    _name = 'guest.family.data'
    _description = "Family Database"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _rec_name = 'combined_name'
    member_ids = fields.One2many('family.member.data', 'family_id', string='Members')

    lastname = fields.Char('Last Name', required=True, tracking=True)
    firstname = fields.Char('First Name', required=True, tracking=True)
    number_of_years_return = fields.Integer()
    cabin_owner = fields.Boolean(default=False)
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
    phone2 = fields.Char()
    email = fields.Char()
    email2 = fields.Char()
    website = fields.Char()
    tag_ids = fields.Many2many('family.data.tag', string='Tags')
    reservation_ids = fields.Many2many('reservation.reservation', 'reservation_family_rel', 'family_id',
                                       'reservation_id',
                                       string='Reservations')
    combined_name = fields.Char(string='Combined Name', compute='_compute_combined_name', store=True)




    @api.depends('firstname', 'lastname')
    def _compute_combined_name(self):
        for record in self:
            # format the datetime fields as per your requirements
            record.combined_name = "%s - %s" % (record.firstname, record.lastname)

    def create_new_reservation(self):
        # Logic to create a reservation
        new_reservation = self.env['reservation.reservation'].create({
            'family_ids': [(6, 0, self.ids)],  # This will add current family into the newly created reservation
            # populate other required fields
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'reservation.reservation',
            'view_mode': 'form',
            'res_id': new_reservation.id,
        }

    def write(self, vals):
        res = super(GuestFamilyData, self).write(vals)
        if 'reservation_ids' in vals:
            for family in self:
                for reservation in family.reservation_ids:
                    # Add new members to reservations
                    for member in family.member_ids.filtered(lambda m: m.is_coming):
                        existing_member = self.env['reservation.member'].search(
                            [('reservation_id', '=', reservation.id), ('member_id', '=', member.id)], limit=1)
                        if not existing_member:
                            self.env['reservation.member'].create({
                                'member_id': member.id,
                                'reservation_id': reservation.id,
                            })
        return res


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
    reservation_member_ids = fields.One2many(
        comodel_name='reservation.member',
        inverse_name='member_id',
        string='Reservation Members'
    )

    def write(self, vals):
        res = super(FamilyMembersData, self).write(vals)

        for record in self:
            # Ensure reservations are updated only if member is marked as 'coming'
            if record.is_coming:
                family_reservations = record.family_id.reservation_ids
                for reservation in family_reservations:
                    existing_member = self.env['reservation.member'].search([
                        ('reservation_id', '=', reservation.id),
                        ('member_id', '=', record.id)
                    ], limit=1)

                    # If no existing reservation member, create it
                    if not existing_member:
                        self.env['reservation.member'].create({
                            'member_id': record.id,
                            'reservation_id': reservation.id,
                        })

        return res

    @api.model
    def create(self, vals):
        # Create the family member first
        record = super(FamilyMembersData, self).create(vals)

        # If the family member is 'coming', link them to all reservations on the family
        if record.is_coming and record.family_id:
            family_reservations = record.family_id.reservation_ids
            for reservation in family_reservations:
                # Check if a reservation.member entry already exists, if not create it
                self.env['reservation.member'].create({
                    'member_id': record.id,
                    'reservation_id': reservation.id,
                })

        return record

    @api.depends("birthdate")
    def _compute_age(self):
        for record in self:
            age = 0
            if record.birthdate:
                age = relativedelta(fields.Date.today(), record.birthdate).years
            record.age = age


