# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ModelesHoraire(models.Model):
    _name = 'modeles.horaire'
    _order = 'id'

    id = fields.Integer(string='id')
    name = fields.Char(string='Horaire',
                       required=True)
    nbrHeuresJour = fields.Float(string="Nombre d'heures")
    totalHeuresHebdo = fields.Float(compute="_compute_totalHeuresHebdo", string="Total hebdomadaire")

    @api.multi
    @api.depends('nbrHeuresJour')
    def _compute_totalHeuresHebdo(self):
        for record in self:
            record.totalHeuresHebdo += record.nbrHeuresJour
