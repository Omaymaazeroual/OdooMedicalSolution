from odoo import models, fields

class Consultation(models.Model):
    _name = 'medical.consultation'

    motif = fields.Char()
    consultationDate = fields.Date()
    price = fields.Float()
    prescription = fields.Many2one('medical.prescription')
    medical_file = fields.Many2one('medical.medical_file', string='Medical File')

