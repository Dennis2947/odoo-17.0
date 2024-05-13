from odoo import http
from odoo.http import request

class PosController(http.Controller):

    @http.route('/pos/mpesa_payment', auth='public', type='http', methods=['POST'], website=True)
    def pos_mpesa_payment(self, **kwargs):
        pos_order_id = kwargs['pos_order_id']
        pos_order = request.env['pos.order'].sudo().browse(pos_order_id)
        if pos_order:
            pos_order.write({
                'mpesa_payment_id': kwargs['mpesa_payment_id'],
            })
        return request.redirect('/pos/payment/validate')
