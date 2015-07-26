# -*- coding: utf-8 -*-
{
    'name': "Recrutement V3",

    'summary': """
        gerer le recrutement facilement v3""",

    'description': """
        Ce module permet de gerer l'activité de recrutement ....
    """,

    'author': "MLMConseil",
    'website': "http://www.mlmconseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Rssources Humaines',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
		
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}