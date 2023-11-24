{
    'name': 'Guestlist',
    'version': '0.5',
    'description': """
    'category': 'Tools',
===================================================
""",
    'depends': ["contacts", "hotel", "ranch_partner_data"],
    'data': [
        'security/ir.model.access.csv',
        'wizards/guestlist_report_wizard_view.xml',
        'report/guestlist_report_template.xml',
        'wizards/guestlist_display_report_wizard_view.xml',
        'report/guestlist_report_display_template.xml',
        'wizards/guestlist_kitchen_report_wizard_view.xml',
        'report/guestlist_report_kitchen_template.xml',
        'wizards/guestlist_barn_report_wizard_view.xml',
        'report/guestlist_report_barn_template.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'auto_install': False,
}
