{
    'name': 'Guestlist',
    'version': '0.2',
    'description': """
    'category': 'Tools',
===================================================
""",
    'depends': ["contacts", "hotel"],
    'data': [
        'security/ir.model.access.csv',
        'wizard/guestlist_report_wizard_view.xml',
        'report/guestlist_report_template.xml',
        'wizard/guestlist_display_report_wizard_view.xml',
        'report/guestlist_report_display_template.xml',
        'views/menus.xml',

    ],
    'installable': True,
    'auto_install': False,
}