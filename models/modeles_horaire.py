# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ModelesHoraire(models.Model):
    _name = 'modeles.horaire'
    _order = 'id'

    horaire_id = fields.Many2one(comodel_name='modeles.signaletique',
                                 string='Nom du modèle')
    name = fields.Char(string='Horaire',
                       required=True)
    semaine = {
        'Lundi': 0,
        'Mardi': 0,
        'Mercredi': 0,
        'Jeudi': 0,
        'Vendredi': 0,
        'Samedi': 0,
        'Dimanche': 0
    }

    nbrHeuresJour = fields.Float(string="Nombre d'heures")
    totalHeuresHebdo = fields.Float(compute="_compute_totalHeuresHebdo", string="Total hebdomadaire")

    @api.depends('nbrHeuresJour')
    def _compute_totalHeuresHebdo(self):
        for record in self:
            record.totalHeuresHebdo += record.nbrHeuresJour
