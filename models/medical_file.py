from odoo import models, fields

class MedicalFile(models.Model):
    _name = 'medical.medical_file'

    id = fields.Char()
    consultations = fields.One2many('medical.consultation', 'medical_file', string='Consultations')
    patient = fields.Many2one('medical.patient', string='Patient')
     # New field for attachments
    attachments = fields.Binary(string='Attachments')