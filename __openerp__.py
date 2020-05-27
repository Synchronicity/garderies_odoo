# -*- coding: utf-8 -*-
{
    'name': "garderies_Odoo",

    'summary': """
        Instruction Publique
        Test/Tuto attributions Garderies""",

    'description': """
        Test/Tuto de gestion des signalétiques des gardiennes, des établissements scolaires et des différents
        éléments nécessaires à l'attribution de prestations en vue du remplacement du programme actuel écrit en VBA.
    """,

    'author': "JLS_181127-191205",
    'website': "http://192.168.56.102:8069",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Instruction Publique',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['web_domain_field', 'extraschool'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu_garderies.xml',
        'views/signaletique_views.xml',
        'views/horaire_views.xml',
        'views/ecole_views.xml',
        'views/implant_views.xml',
        'views/prestation_views.xml',
        'views/conge_views.xml',
        'views/ferie_views.xml',
        'views/templates.xml',
        'views/vacances_calendrier_views.xml',
        'views/modeles_signaletique_views.xml',
        'views/modeles_horaire_views.xml',
    ],
}
