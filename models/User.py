from odoo import models, fields

class User(models.Model):
    _name = 'medical.user'


    firstName = fields.Char()
    lastName = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    password = fields.Char()
