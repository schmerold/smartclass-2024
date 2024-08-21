import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    spaceship_ids = fields.One2many(comodel_name='space.spaceship', string="Spaceships", inverse_name="partner_id")