from odoo import models, fields

class ModelOne(models.Model):
	
	_name = "model.one"
	_description = "Model One"


	#feilds
	name = fields.Char(string="Name", help='A normal name field')
	age = fields.Integer(string="Age")
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
	active = fields.Boolean('Active')
	description = fields.Text("Description")
	joining = fields.Date(string="Joining")
