# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Ferie(models.Model):
    _name = 'garderies.ferie'
    _order = 'date_ferie'

    name = fields.Char(string='Jour férié',
                       required=True)
    date_ferie = fields.Date(string='Date',
                             required=True)
