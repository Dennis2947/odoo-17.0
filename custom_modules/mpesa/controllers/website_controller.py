from odoo import http
from odoo.http import request

class WebsiteController(http.Controller):

    @http.route('/website/mpesa_payment', auth='public', type='http', methods=['POST'], website=True)
    def website_mpesa_payment(self, **kwargs):
        order_id = kwargs['order_id']
        order = request.env['sale.order'].sudo().browse(order_id)
        if order:
            order.write({
                'mpesa_payment_id': kwargs['mpesa_payment_id'],
            })
        return request.redirect('/payment/validate')
