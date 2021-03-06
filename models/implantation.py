# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Implantation(models.Model):
    _name = 'garderies.implantation'
    _order = 'name'

    name = fields.Char(string='Implantation',
                       required=True)
    adresse = fields.Char(string='Adresse',
                          required=True)
    cp_loc = fields.Char(string="CP & Loc",
                         required=True)
    tel = fields.Char(string="Téléphone")

    # DEPENDENCE DE L'ECOLE
    ecole_id = fields.Many2one(comodel_name='garderies.ecole',
                               string='Ecole')
