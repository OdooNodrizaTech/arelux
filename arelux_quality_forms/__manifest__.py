# -*- coding: utf-8 -*-
{
    'name': 'Arelux Quality Forms',
    'version': '12.0.1.0.0',
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'data/waste_remove_product.xml',
        'data/maintenance_installation_need_check_data.xml',
        'data/ir_configparameter_data.xml',
        'data/ir_cron.xml',
        'security/ir.model.access.csv',
        'views/fire_drill_view.xml',
        'views/fire_drill_decision_view.xml',
        'views/maintenance_installation_view.xml',
        'views/maintenance_installation_need_check_view.xml',
        'views/waste_remove_view.xml',
        'views/waste_remove_detail_view.xml',
        'views/waste_remove_product_view.xml',
        'views/menu_view.xml',
    ],
    'installable': True,
    'auto_install': False,    
}