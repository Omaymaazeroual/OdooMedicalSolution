from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'medical.appointment'

    dateofChecking = fields.Date()
    dateofAppointment = fields.Date()
    description = fields.Char()
    typeofIllness = fields.Char()
    notification = fields.Boolean()
    user_id = fields.Many2one('res.users', string='Related User Account')
    patient_id = fields.Many2one('medical.patient', string='Patient')

    @api.model
    def create(self, vals):
        # Set user_id to the currently logged-in user
        vals['user_id'] = self.env.user.id
        return super(Appointment, self).create(vals)
