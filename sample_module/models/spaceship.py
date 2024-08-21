from odoo import api, fields, models

class Spaceship(models.Model):
    """Model used to store information about spaceships"""
    _name = 'space.spaceship'
    _description = 'Spaceship'

    name = fields.Char(string="name")
    manufacture_date = fields.Date(string="Date")
    number = fields.Integer(string="Number")

cost_per_gallon = fields.Float(string="Cost Per Gallon")
gallons_per_tank = fields.Integer(string="Gallons Per Tank")

cost_per_tank = fields.Float(string="Cost To Fill Tank", compute="_compute_cost_per_tank")

partner_id = fields.Many2one(comodel="res.partner", string="Partner")

@api.depends('cost_per_gallon', 'gallons_per_tank')
def _compute_cost_per_tank(self):
    for spaceship in self:
        spaceship.cost_per_tank = spaceship.cost_per_gallon * spaceship.gallons_per_tank
