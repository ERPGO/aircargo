# -*- coding: utf-8 -*-
from odoo import http

# class Aircargo(http.Controller):
#     @http.route('/aircargo/aircargo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aircargo/aircargo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aircargo.listing', {
#             'root': '/aircargo/aircargo',
#             'objects': http.request.env['aircargo.aircargo'].search([]),
#         })

#     @http.route('/aircargo/aircargo/objects/<model("aircargo.aircargo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aircargo.object', {
#             'object': obj
#         })