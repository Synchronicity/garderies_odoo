# -*- coding: utf-8 -*-
{
    'name': "garderies",

    'summary': """
        Instruction Publique
        Test attributions Garderies""",

    'description': """
        Test de gestion des signalétiques des gardiennes, des établissements scolaires et des différents éléments
        nécessaires à l'attribution de prestations en vue du remplacement du vieux programme écrit en VBA.
    """,

    'author': "JLS_181127",
    'website': "http://192.168.56.101:8069",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Instruction Publique',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web_domain_field'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/signaletique_views.xml',
        'views/horaire_views.xml',
        'views/ecole_views.xml',
        'views/implant_views.xml',
        'views/garderies_menu.xml',
        'views/prestation_views.xml',
        'views/conge_views.xml',
        'views/ferie_views.xml',
    ],
}