# -*- coding: utf-8 -*-
from openerp import http

# class Garderies(http.Controller):
#     @http.route('/garderies/garderies/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/garderies/garderies/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('garderies.listing', {
#             'root': '/garderies/garderies',
#             'objects': http.request.env['garderies.garderies'].search([]),
#         })

#     @http.route('/garderies/garderies/objects/<model("garderies.garderies"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('garderies.object', {
#             'object': obj
#         })