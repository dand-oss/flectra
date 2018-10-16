# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.


{
    'name': 'Sales and MRP Management',
    'author': 'Odoo S.A.',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
This module provides facility to the user to install mrp and sales modulesat a time.
====================================================================================

It is basically used when we want to keep track of production orders generated
from sales order. It adds sales name and sales Reference on production order.
    """,
    'website': 'https://flectrahq.com/manufacturing',
    'depends': ['mrp', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test':[
        'test/sale_mrp.yml',
        ],
    'installable': True,
    'auto_install': True,
}
