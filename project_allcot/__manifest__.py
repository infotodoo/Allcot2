# -*- coding: utf-8 -*-
{
    'name': "Allcot project",

    'summary': "Organize and schedule your projects",

    'description': "Organize and schedule your projects",

    'author': "Todoo SAS",
    'contributors': "Juan Arcos pa@todoo,co",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Operations/Project',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['product', 'project_enterprise'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_task_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
