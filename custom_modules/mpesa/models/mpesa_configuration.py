from odoo import models, fields

class MpesaConfiguration(models.Model):
    _name = 'mpesa.configuration'
    _description = 'Mpesa Configuration'
    user_id = fields.Many2one('res.users', string='User')
    session_id = fields.Many2one('pos.session', string='Session')
    partner_id = fields.Many2one('res.partner', string='Partner')
    api_key = fields.Char(string='API Key', required=True)
    password = fields.Char(string='Password', required=True)
    short_code = fields.Char(string='Short Code', required=True)
    business_short_code = fields.Char(string='Business Short Code', required=True)
    passkey = fields.Char(string='Passkey', required=True)
    initiator_name = fields.Char(string='Initiator Name', required=True)
    callback_url = fields.Char(string='Callback URL', required=True)
    account_reference = fields.Char(string='Account Reference', required=True)
    transaction_desc = fields.Char(string='Transaction Description', required=True)

