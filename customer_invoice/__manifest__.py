# -*- coding: utf-8 -*-
{
    'name': "customer_invoice",
    'description': "customer_invoice",
    'author': 'Techistan',
    'website': "http://www.techistan.com",
    'category': 'account',
    'version': '14.0.1.6',
    'application': True,
    'depends': ['base', 'web', 'account_accountant'],
    'data': ['template.xml', 'views/module_report.xml',
             'views/concise_invoice_temp.xml',
             'views/custom_sale_report_template.xml'
             ],

    'installable': True,
    'auto_install': False,
}
