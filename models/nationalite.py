# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Nationalite(models.Model):
    _name = 'garderies.nationalite'
    _order = 'name'

    name = fields.Char(string='Nationalite',
                       required=True)