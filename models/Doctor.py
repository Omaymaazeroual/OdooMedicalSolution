from odoo import models, fields

class Doctor(models.Model):
    _name = 'medical.doctor'
    _inherit = 'medical.user'

    speciality = fields.Char()