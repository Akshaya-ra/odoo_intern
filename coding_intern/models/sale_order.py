from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    model_one_id = fields.Many2one('model.one', string="Model One")
    description = fields.Text(string="Description")  # Added string attribute
    
    @api.depends('partner_id')
    def _compute_partner_invoice_id(self):
        res = super(SaleOrder, self)._compute_partner_invoice_id()
        for order in self:
            order.description = "Added by a method"
        return res