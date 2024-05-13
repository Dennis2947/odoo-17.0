# -*- coding: utf-8 -*-
{
    'name': "Mpesa Express",

    'summary': "Mpesa Payment Method",

    'description': """
Long description of module's purpose
    """,

    'author': "Dennis Nyagah",
    'website': "https://www.flowcode.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menu.xml',
        'views/pos_order_view.xml',
        'views/sale_order_view.xml',
        'views/mpesa_payment_view.xml',
        'views/mpesa_configuration_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

