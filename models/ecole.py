# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Ecole(models.Model):
    _inherit = 'extraschool.school'
    _name = 'garderies.ecole'
    # _order = 'name'

    # name = fields.Char(string='Ecole',
    #                   required=True)
    adresse = fields.Char(string='Adresse',
                          required=True)
    cp_loc = fields.Char(string="CP & Loc",
                         required=True)
    num_bat = fields.Integer(string="Numéro bâtiment")
    titre = fields.Selection([('0', 'Madame'), ('1', 'Monsieur')], 'Titre')
    nom_dir = fields.Char(string="Direction")
    tel = fields.Char(string="Téléphone")

    # IMPLANTATION(S) DE L'ECOLE
    implantation_ids = fields.One2many(comodel_name='garderies.implantation', inverse_name='ecole_id',
                                       string='Implantation(s)',
                                       help="Implantation(s) de l'école")
