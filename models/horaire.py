# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Horaire(models.Model):
    _name = 'garderies.horaire'
    _order = 'name'

    id = fields.Integer(string='id')
    name = fields.Char(string='Horaire',
                       required=True)
    debut = fields.Float(string='Début')
    fin = fields.Float(string='Fin')
