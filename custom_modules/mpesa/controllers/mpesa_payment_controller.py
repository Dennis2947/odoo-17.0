from odoo import http
from odoo.http import request

class MpesaPaymentController(http.Controller):

    @http.route('/mpesa/payment', auth='public', type='http', methods=['GET'], website=True)
    def mpesa_payment(self, **kwargs):
        values = {}
        order_id = kwargs['order_id']
        order = request.env['sale.order'].sudo().browse(order_id)
        if order:
            values['order'] = order
        return request.render('mpesa.mpesa_payment_view', values)

    @http.route('/mpesa/payment/save', auth='public', type='http', methods=['POST'], website=True)
    def mpesa_payment_save(self, **kwargs):
        order_id = kwargs['order_id']
        order = request.env['sale.order'].sudo().browse(order_id)
        if order:
            order.write({
                'mpesa_payment_id': kwargs['mpesa_payment_id'],
            })
        return request.redirect('/payment/process')
