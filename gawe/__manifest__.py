# -*- coding: utf-8 -*-
{
    'name': "Gawe",

    'summary': """
        Module Gawe cinte""",

    'description': """
        Manajemen Gawe
    """,

    'author': "Dynasti",
    'website': "https::/cinte.id",

    'category': 'Uncategorized',
    'version': '0.1',

		# Depencicy
    'depends': [
        'base',
        'web_editor',
    ],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        'view/menuitems.views.xml',
        'view/ticket.action.views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}
