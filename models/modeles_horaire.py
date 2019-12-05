# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ModelesHoraire(models.Model):
    _name = 'modeles.horaire'
    _order = 'id'

    id = fields.Integer(string='id')
    name = fields.Char(string='Horaire',
                       required=True)
    nbrHeuresJour = fields.Float(string="Nombre d'heures")
    totalHeuresHebdo = fields.Float(string="Total hebdomadaire")

    # def _totalHeuresHebdo(self):
    #     for hours in self:
    #         ModelesHoraire.totalHeuresHebdo += hours.nbrHeuresJour
