# -*- coding: utf-8 -*-
from openerp import models, fields, api


class VacancesCalendrier(models.Model):
    _name = "vacances.calendrier"
    _order = "debut_vacances"

    name = fields.Char(string='Vacances ou férié',
                       required=True)
    debut_vacances = fields.Date(string='Début',
                        required=True)
    fin_vacances = fields.Date(string='Fin',
                      required=True)
