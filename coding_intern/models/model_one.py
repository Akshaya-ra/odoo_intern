from odoo import models, fields , api

class ModelOne(models.Model):
	
	_name = "model.one"
	_description = "Model One"


	#feilds
      
	seq = fields.Char(string="Sequence")
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
	model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id', string="Product")
      
	
	def helloworld(self):
		print("hello world")

	# display a wizard through button action

 
	def show_wizard(self):
 
		return {
            'type': 'ir.actions.act_window',
            'name': 'My Sample Wizard',
            'res_model': 'sample.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('coding_intern.view_form_sample_wizard').id,
            'target': 'new',
			'context' : {'default_name': 'Akshaya'}
        }	
	
	
	@api.model
	def create(self,vals):
		vals['seq'] = self.env['ir.sequence'].next_by_code('sequence.model.one')
		res = super (ModelOne, self).create(vals)
		return res
    
 
class ModelOnelines(models.Model):
    _name = "model.one.lines"
    _description = "Model One lines"
 
    name = fields.Char(string="Name", help='A normal name field')
    price = fields.Float(string="Price")
    product_id = fields.Many2one('product.template', string="Product")
    model_one_id = fields.Many2one('model.one', string="Model One", domain="['|', ('gender','=', 'female'),('age', '>', 18)]")

	# create_date = fields.Datetime(string="Created Date") # please use BASE fields (create_date,create_uid)
    