from odoo import models, fields

class Prescription(models.Model):
    _name = 'medical.prescription'


    title = fields.Char()
    dateOfPrescription = fields.Date()
    description = fields.Char()
    medicationList = fields.Char()