{
    'name': 'Ranch Partner data',
    'version': '0.3',
    'category': 'Hidden',
    'description': """Ranch related fields for partners
    "author": "typecookie"
    "summary": "ranchAddons"
===================================================
""",
    'depends': ["contacts", "hotel_reservation"],
    'data': [
        "security/ir.model.access.csv",
        'wizards/horse_assign_wizard_views.xml',
        'wizards/horse_assign_update_wizard_views.xml',
        'views/ranch_contact_fields_view.xml',
        'views/horse_assign_data_views.xml',
        'wizards/saddle_assign_wizard_views.xml',
        'wizards/saddle_assign_update_wizard_views.xml',

    ],
    "installable": True,

}
