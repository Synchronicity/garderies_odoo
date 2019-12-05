# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ModelesHoraire(models.Model):
    _name = 'modeles.horaire'
    _order = 'name'

    id = fields.Integer(string='id')
    name = fields.Char(string='Horaire',
                       required=True)
    nbrHeures = fields.Float(string="Nombre d'heures")
