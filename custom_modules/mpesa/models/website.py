from odoo import models, fields

class WebsiteOrder(models.Model):
    _inherit = 'sale.order'
    partner_id = fields.Many2one('res.partner', string='Partner')
    mpesa_payment_id = fields.Many2one('mpesa.payment', string='M-PESA Payment')
