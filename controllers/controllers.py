# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/alquiler(http.Controller):
#     @http.route('/extra-addons/alquiler/extra-addons/alquiler/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/alquiler/extra-addons/alquiler/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/alquiler.listing', {
#             'root': '/extra-addons/alquiler/extra-addons/alquiler',
#             'objects': http.request.env['extra-addons/alquiler.extra-addons/alquiler'].search([]),
#         })

#     @http.route('/extra-addons/alquiler/extra-addons/alquiler/objects/<model("extra-addons/alquiler.extra-addons/alquiler"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/alquiler.object', {
#             'object': obj
#         })