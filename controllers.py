# -*- coding: utf-8 -*-
from openerp import http

# class C:\users\dell\documents\odooTest\hrRecrutement(http.Controller):
#     @http.route('/c:\users\dell\documents\odoo_test\hr_recrutement/c:\users\dell\documents\odoo_test\hr_recrutement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\dell\documents\odoo_test\hr_recrutement/c:\users\dell\documents\odoo_test\hr_recrutement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\dell\documents\odoo_test\hr_recrutement.listing', {
#             'root': '/c:\users\dell\documents\odoo_test\hr_recrutement/c:\users\dell\documents\odoo_test\hr_recrutement',
#             'objects': http.request.env['c:\users\dell\documents\odoo_test\hr_recrutement.c:\users\dell\documents\odoo_test\hr_recrutement'].search([]),
#         })

#     @http.route('/c:\users\dell\documents\odoo_test\hr_recrutement/c:\users\dell\documents\odoo_test\hr_recrutement/objects/<model("c:\users\dell\documents\odoo_test\hr_recrutement.c:\users\dell\documents\odoo_test\hr_recrutement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\dell\documents\odoo_test\hr_recrutement.object', {
#             'object': obj
#         })