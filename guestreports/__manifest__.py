{
    'name': 'Guestlist',
    'version': '0.1',
    'description': """
    'category': 'Tools',
===================================================
""",
    'depends': ["contacts", "hotel"],
    'data': [
        'security/ir.model.access.csv',
        'wizard/guestlist_report_wizard_view.xml',
        'report/guestlist_report_template.xml',
        'views/menus.xml',

    ],
    'installable': True,
    'auto_install': False,
}