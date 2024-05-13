from odoo import http
from odoo.http import request

class MpesaConfigurationController(http.Controller):

    @http.route('/mpesa/configuration', auth='public', type='http', methods=['GET'], website=True)
    def mpesa_configuration(self, **kwargs):
        values = {}
        mpesa_config = request.env['mpesa.configuration'].sudo().search([])
        if mpesa_config:
            values['mpesa_config'] = mpesa_config[0]
        return request.render('mpesa.mpesa_configuration_view', values)

    @http.route('/mpesa/configuration/save', auth='public', type='http', methods=['POST'], website=True)
    def mpesa_configuration_save(self, **kwargs):
        mpesa_config = request.env['mpesa.configuration'].sudo()
        if 'id' in kwargs:
            mpesa_config = mpesa_config.browse(kwargs['id'])
        mpesa_config.write({
            'active': bool(int(kwargs['active'])),
            'business_short_code': kwargs['business_short_code'],
            'passkey': kwargs['passkey'],
            'lipa_na_mpesa_online_password': kwargs['lipa_na_mpesa_online_password'],
            'lipa_na_mpesa_online_short_code': kwargs['lipa_na_mpesa_online_short_code'],
            'callback_url': kwargs['callback_url'],
            'account_reference': kwargs['account_reference'],
            'transaction_desc': kwargs['transaction_desc'],
        })
        return request.redirect('/mpesa/configuration')
