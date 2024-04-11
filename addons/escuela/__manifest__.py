# -*- coding: utf-8 -*-
{#nombre del modulo
    'name': "escuela",
#descripcion general del modulo enfocada en su funcionalidad
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "alan",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    #version, es variable ya que puede haber varias versiones
    'category': 'Recursos Humanos',
    'version': '0.1',
    'installable': True,  #indicmos para indicar que si es instalable
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    #aqui se especifica los archivos xml que forman parte los modulos o los formularios que iran integradfods 
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
