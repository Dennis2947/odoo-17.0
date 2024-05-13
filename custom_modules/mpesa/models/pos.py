from odoo import api, fields, models


class PosOrder(models.Model):
    _name = 'pos.order'
    _inherits = 'pos.payment'
    _description = 'Point of Sale Order'

    payment_ids = fields.One2many('pos.payment', string='Payments', readonly=True, copy=False)
    session_id = fields.Many2one('pos.session', string='Session')
    currency_id = fields.Many2one('res.currency', string='Currency')
    account_move = fields.Many2one('account.move', string='Account Move')
    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default='New')
    date_order = fields.Datetime(string='Date Order', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='User', required=True, readonly=True, index=True, default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, index=True, default=lambda self: self.env.company)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, readonly=True, index=True, states={'draft': [('readonly', False)]})
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist', required=True, readonly=True, index=True, default=lambda self: self.env.company.pricelist_id)
    fiscal_position_id = fields.Many2one('account.fiscal.position', string='Fiscal Position', readonly=True, index=True, states={'draft': [('readonly', False)]}, copy=False)
    line_ids = fields.One2many('pos.order.line', 'order_id', string='Order Lines', readonly=True, states={'draft': [('readonly', False)]})
    amount_total = fields.Float(string='Total', store=True, readonly=True, compute='_compute_amount_total')
    amount_paid = fields.Float(string='Amount Paid', store=True, readonly=True, compute='_compute_amount_paid')
    amount_return = fields.Float(string='Amount Return', store=True, readonly=True, compute='_compute_amount_return')
    amount_tax = fields.Float(string='Amount Tax', store=True, readonly=True, compute='_compute_amount_tax')
    amount_untaxed = fields.Float(string='Amount Untaxed', store=True, readonly=True, compute='_compute_amount_untaxed')
    refund_orders_count = fields.Integer(string='Refund Orders Count', compute='_compute_refund_related_fields')
    refund_orderline_ids = fields.Many2many('pos.order.line', string='Refund Order Lines')

    # Computed Fields
    @api.depends('line_ids')
    def _compute_amount_total(self):
        for record in self:
            record.amount_total = sum(line.price_subtotal_incl for line in record.line_ids)

    @api.depends('line_ids')
    def _compute_amount_paid(self):
        for record in self:
            record.amount_paid = sum(line.price_total for line in record.line_ids)

    @api.depends('line_ids')
    def _compute_amount_return(self):
        for record in self:
            record.amount_return = sum(line.price_return for line in record.line_ids)

    @api.depends('line_ids')
    def _compute_amount_tax(self):
        for record in self:
            record.amount_tax = sum(line.price_tax for line in record.line_ids)

    @api.depends('line_ids')
    def _compute_amount_untaxed(self):
        for record in self:
            record.amount_untaxed = sum(line.price_subtotal for line in record.line_ids)

    @api.depends('refund_orderline_ids')
    def _compute_refund_related_fields(self):
        for record in self:
            record.refund_orders_count = len(record.refund_orderline_ids.mapped('order_id'))

    @api.depends('payment_ids')
    def _compute_total_payments_amount(self):
        for session in self:
            session.total_payments_amount = sum(payment.amount for payment in session.payment_ids)
