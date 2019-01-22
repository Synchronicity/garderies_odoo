# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Conge(models.Model):
    _name = 'garderies.conge'
    _order = 'debut desc'

    debut = fields.Date(string='Début',
                        required=True)
    fin = fields.Date(string="Fin")
    type = fields.Selection([('0', 'Récupération'), ('1', 'Vacances'), ('2', 'Grève')], 'Type de congé')

    # CONGÉS DE L'AGENT
    conge_id = fields.Many2one(comodel_name='garderies.signaletique',
                               string='Agent')
    name = conge_id
