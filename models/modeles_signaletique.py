# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ModelesSignaletique(models.Model):
    _name = 'modeles.signaletique'
    _order = 'name'

    name = fields.Char(string='Nom',
                       required=True)
    prenom = fields.Char(string='Prénom',
                         required=True)
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
                              ('4', 'Péd.')],
                             'Titre')
    matricule = fields.Integer(string="Matricule ULIS")
    date_in = fields.Date(string="Date d'entrée")
    rem = fields.Text(string='Remarques & infos')

    # CHOIX DE LA NATIONALITE
    nationalite = fields.Many2one(comodel_name='garderies.nationalite',
                                  string='Nationalité')
    # DESIGNATION DE L'HORAIRE
    horaire_id = fields.Many2many(comodel_name='modeles.horaire',
                                  string='Horaire')
    # LISTE DES CONGÉS
    conge_ids = fields.One2many(comodel_name='garderies.conge', inverse_name='conge_id',
                                string='Congé(s)')
    # PRESTATIONS
    prestation_ids = fields.One2many(comodel_name='garderies.prestation', inverse_name='name',
                                     string='Prestation(s)',
                                     help="Prestation(s) du modèle")