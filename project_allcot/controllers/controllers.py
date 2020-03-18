# -*- coding: utf-8 -*-
# from odoo import http


# class AllcotProject(http.Controller):
#     @http.route('/project_allcot/project_allcot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_allcot/project_allcot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_allcot.listing', {
#             'root': '/project_allcot/project_allcot',
#             'objects': http.request.env['project_allcot.project_allcot'].search([]),
#         })

#     @http.route('/project_allcot/project_allcot/objects/<model("project_allcot.project_allcot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_allcot.object', {
#             'object': obj
#         })
