{
    'name': 'Guestlist',
    'version': '16.0.1.0.0',
    'description': """
    'category': 'Tools',
===================================================
""",
    'depends': ["contacts", "hotel", "ranch_partner_data", "base_setup"],
    'data': [
        'security/ir.model.access.csv',
        'wizard/guestlist_report_wizard_view.xml',
        'views/menus.xml',
        'report/guestlist_report_template.xml',
    ],
    'assets': {
        'web.assets_backend_legacy_lazy': ["guestreports/static/src/**/*", ]
    },
    'css': ['guestreports/static/src/css/styles.css'],

    'installable': True,
    'auto_install': False,
}
