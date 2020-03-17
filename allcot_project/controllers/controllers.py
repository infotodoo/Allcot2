# -*- coding: utf-8 -*-
# from odoo import http


# class AllcotProject(http.Controller):
#     @http.route('/allcot_project/allcot_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/allcot_project/allcot_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('allcot_project.listing', {
#             'root': '/allcot_project/allcot_project',
#             'objects': http.request.env['allcot_project.allcot_project'].search([]),
#         })

#     @http.route('/allcot_project/allcot_project/objects/<model("allcot_project.allcot_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('allcot_project.object', {
#             'object': obj
#         })
