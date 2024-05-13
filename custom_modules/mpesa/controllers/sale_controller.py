from odoo import http
from odoo.http import request

class SaleController(http.Controller):

    @http.route('/sale/mpesa_payment', auth='public', type='http', methods=['POST'], website=True)
    def sale_mpesa_payment(self, **kwargs):
        sale_order_id = kwargs['sale_order_id']
        sale_order = request.env['sale.order'].sudo().browse(sale_order_id)
        if sale_order:
            sale_order.write({
                'mpesa_payment_id': kwargs['mpesa_payment_id'],
            })
        return request.redirect('/sale/payment/validate')
