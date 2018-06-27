# -*- coding: utf-8 -*-
{
    'name': "Alquiler",

    'summary': """
        Modulo de alquiler como prueba para el puesto de desarrollador""",

    'description': """
        Es una serie de funciones que fueron mencionadas en las instrucciones
    """,

    'author': "Lenynd Bermudez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_invoicing','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
}