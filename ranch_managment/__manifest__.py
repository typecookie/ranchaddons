{
    'name': 'Ranch Management',
    'version': 'rc-0.4',
    'category': 'Tools',
    'description': """
    "author": "typecookie"
    "summary": "ranchAddons"
===================================================
""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/horses_main_view.xml',
        'views/saddle_main_view.xml',
        'views/menus.xml',
        'views/company_ranch_date_view.xml',
        'wizards/vet_wizard_views.xml',
        'wizards/horse_vitals_wizard_views.xml'

    ],
    'installable': True,
    'auto_install': False,
}
