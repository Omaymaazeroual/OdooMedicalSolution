from odoo import models, fields

class Patient(models.Model):
    _name = 'medical.patient'
    _inherit = 'medical.user'


    birthDate = fields.Date()
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female')
        ], string='gender')
    # Add a Many2one field to link the patient to a user
    user_id = fields.Many2one('res.users', string='Related User Account')