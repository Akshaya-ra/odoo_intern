from odoo import models, fields

class ModelOne(models.Model):
	
	_name = "model.one"
	_description = "Model One"


	#feilds
	name = fields.Char(string="Name", help='A normal name field')
	age = fields.Integer(string="Age")
	name = fields.Char(string="Name", help='You can add your name here', copy=False)
	age = fields.Integer(string="Age", default=18)
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, copy=False,default='male')
	active = fields.Boolean('Active')
	description = fields.Text("Description")
	description = fields.Text("Description", default="Test Description")
	create_date = fields.Date("Created Date")
	# create_date = fields.Datetime(string="Created Date") # please use BASE fields (create_date,create_uid)
    