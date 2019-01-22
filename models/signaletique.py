# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Signaletique(models.Model):
    _name = 'garderies.signaletique'
    _order = 'name'

    name = fields.Char(string='Nom',
                       required=True)
    prenom = fields.Char(string='Prénom',
                         required=True)
    candidat = fields.Selection([('0', 'Agent'), ('1', 'Validé'), ('2', 'Auditionné'),
                                 ('3', 'Candidat'), ('4', 'Refusé')],
                                'Statut')
    adresse = fields.Char(string='Adresse',
                          required=True)
    cp = fields.Integer(string="Code postal",
                        required=True)
    localite = fields.Char(string="Localité",
                           required=True)
    nn = fields.Char(string="Numéro National",
                     required=True)
    sexe = fields.Selection([('0', 'F'), ('1', 'M')],
                            'Sexe')
    tel = fields.Char(string="Téléphone")
    email = fields.Char(string="e-mail")
    titre = fields.Selection([('0', 'Aucun'), ('1', 'Prim. et S.I.'), ('2', 'S.S.'), ('3', 'Sup. non Péd.'),
                              ('4', 'Péd.'), ('5', 'Monit. collect. enf.'), ('6', 'Puéri.'), ('7', 'Brevet CEMEA'),
                              ('8', 'Formation Ville'), ('9', 'Formation 40')],
                             'Titre')
    matricule = fields.Integer(string="Matricule ULIS")
    date_in = fields.Date(string="Date d'entrée")
    rem = fields.Char(string='Remarques')

    # CHOIX DE LA NATIONALITE
    nationalite = fields.Many2one(comodel_name='garderies.nationalite',
                                  string='Nationalité')
    # CHOIX DES HORAIRES ACCEPTES
    horaire_id = fields.Many2many(comodel_name='garderies.horaire',
                                  string='Horaire(s)')
    # LISTE DES CONGÉS
    conge_ids = fields.One2many(comodel_name='garderies.conge', inverse_name='conge_id',
                                string='Congé(s)')
    # PRESTATIONS
    prestation_ids = fields.One2many(comodel_name='garderies.prestation', inverse_name='name',
                                     string='Prestation(s)',
                                     help="Prestation(s) de l'agent")
