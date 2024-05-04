from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class VehicleData(models.Model):
    _name = 'vehicle.data'
    _description = "Vehicle Database"
    # _inherit = 'image.mixin'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'vin'

    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Char(string='Year')
    mileage = fields.Float(string='Mileage')
    hours = fields.Float(string='Hours')
    vin = fields.Char(string='VIN')
    purchase_date = fields.Date(string='Purchase Date')
    purchase_price = fields.Float(string='Purchase Price')
    tire_pressure = fields.Float(string='Tire Pressure')
##    part_install_id = fields.One2many('vehicle.parts', 'vin', string='Part Install ID')
    maintenance_id = fields.One2many('vehicle.maintenance', 'vin', string='Maintenance ID')
##    part_list_id = fields.One2many('vehicle.parts', 'vin', string='Part List ID')


##class VehiclePartsInstall(models.Model):
##    _name = 'vehicle.parts'
##    _description = "Vehicle Parts"
##
##    part_name = fields.Char(string='Part Name')
##    part_number = fields.Char(string='Part Number')
##    installed_on_date = fields.Date(string='Installed On Date')
##    vin = fields.Char(string='VIN')


class VehicleMaintenance(models.Model):
    _name = 'vehicle.maintenance'
    _description = "Vehicle Maintenance"
    _rec_name = 'vin'

    date = fields.Date(string='Maintenance Date')
    mileage = fields.Float(string='Mileage')
    shop = fields.Char(string='Shop')
    oil_change = fields.Boolean(string='Oil Change')
    air_filter = fields.Boolean(string='Air Filter')
    tire_rotate = fields.Boolean(string='Tire Rotate')
    checkup = fields.Boolean(string='Checkup')
    grease = fields.Boolean(string='Grease')
    washer_fluid = fields.Boolean(string='Washer Fluid')
    hydraulic_fluid = fields.Boolean(string='Hydraulic Fluid')
    vin = fields.Char(string='VIN')
##class VehiclePartsList(models.Model):
##    _name = 'vehicle.parts.list'
##    _description = "Vehicle Parts List"
##
##    part_name = fields.Char(string='Part Name')
##    part_number = fields.Char(string='Part Number')
##    vin = fields.Char(string='VIN')
##
class HorseVitals(models.Model):
    _name = 'horse.vitals'
    _description = "Vitals DB"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(tracking=True)
    Temp = fields.Char(tracking=True)
    BPM = fields.Char(tracking=True)
    Notes = fields.Char(tracking=True)
