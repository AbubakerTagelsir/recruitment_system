# -*- coding: utf-8 -*-
{
    'name': "Recruitment",

    'summary': """
       Job seeking system""",

    'description': """
        
    """,

    'author': "Aml Kamal",
    'website': "amlbabikir@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        'security/users_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
