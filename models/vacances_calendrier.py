# -*- coding: utf-8 -*-
from openerp import models, fields, api


class VacancesCalendrier(models.Model):
    _name = "vacances.calendrier"

    name = fields.Char(string='Jour',
                       required=True)
