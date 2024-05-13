from odoo import models, fields

class MpesaPayment(models.Model):
    _name = 'mpesa.payment'
    session_id = fields.Many2one('pos.session', string='Session')
    currency_id = fields.Many2one('res.currency', string='Currency')
    partner_id = fields.Many2one('res.partner', string='Partner')
    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
    transaction_date = fields.Datetime(string='Transaction Date', required=True)
    order_id = fields.Many2one('sale.order', string='Order', required=True)
