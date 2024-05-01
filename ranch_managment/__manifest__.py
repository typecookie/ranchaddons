{
    'name': 'Ranch Management',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'license': "AGPL-3",
    'description': """===================================================""",
    'author': "typecookie",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/horse_vitals_wizard_views.xml',
        'wizards/vet_wizard_views.xml',
        'views/horses_main_view.xml',
        'views/saddle_main_view.xml',
        'views/company_ranch_date_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
