from odoo import models, fields

class Event(models.Model):
    _name = 'event.management'
    _description = 'Event Management'

    name = fields.Char('Event Name', required=True)
    start_date = fields.Datetime('Start Date', required=True)
    end_date = fields.Datetime('End Date')
    location = fields.Char('Location')
    description = fields.Text('Description')
    attendee_count = fields.Integer('Attendees')  # Manual update instead of compute
    attendee_ids = fields.One2many('event.attendee', 'event_id', 'Attendees')

class EventAttendee(models.Model):
    _name = 'event.attendee'
    _description = 'Event Attendee'

    name = fields.Char('Attendee Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    event_id = fields.Many2one('event.management', 'Event')