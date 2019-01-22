# -*- coding: utf-8 -*-
import json
from openerp import models, fields, api


class Prestation(models.Model):
    _name = 'garderies.prestation'
    _order = 'name, debut desc'

    # AGENT PRESTANT
    name = fields.Many2one(comodel_name='garderies.signaletique',
                           string='Agent')
    debut = fields.Date(string='Début',
                        required=True)
    fin = fields.Date(string='Fin',
                      required=True)
    # HORAIRE POUR LA PRESTATION
    horaire_id = fields.Many2one(comodel_name='garderies.horaire',
                                 string='Horaire',
                                 help="Plage horaire de la prestation",
                                 required=True)
    # HORAIRES POSSIBLES DE L'AGENT
    horaire_id_domain = fields.Char(
        compute="_compute_horaire_id_domain",
        readonly=True,
        store=False,
    )

    # LIEU DE LA PRESTATION
    implant_id = fields.Many2one(comodel_name='garderies.implantation',
                                 string='Etablissement',
                                 required=True)

    remplace_agent = fields.Many2one('garderies.signaletique', "Remplace l'agent")
    remplace_motif = fields.Char('Motif')
    empty_line = fields.Char(' ')
    absence_debut = fields.Date('Début absence')
    absence_fin = fields.Date('Fin absence')
    absence_motif = fields.Char("Motif absence")

    @api.multi
    @api.depends('name')
    def _compute_horaire_id_domain(self):
        ids = []
        for hor in self.name.horaire_id:
            ids.append(hor.id)

        for rec in self:
            rec.horaire_id_domain = json.dumps(
                [((('id','in', ids)))]
            )

    # @api.onchange('name')
    # def agent_horaire(self):
    #     self.horaire_id = self.name.horaire_id
