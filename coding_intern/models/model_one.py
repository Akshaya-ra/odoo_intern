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
	partner_ids = fields.Many2many ('res.partner' , string="Partner")
	sale_ids = fields.Many2many('sale.order','model_one_sale_rel','model_one_id','sale_id', string="Sale")
	product_ids = fields.Many2many('product.template','model_one_product_rel','model_one_id','product_id', string="product")

	# create_date = fields.Datetime(string="Created Date") # please use BASE fields (create_date,create_uid)
    