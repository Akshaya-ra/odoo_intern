{
    'name': 'Event Management',
    'version': '1.0',
    'summary': 'Basic Event Management System',
    'description': 'Manage events, attendees, and schedules',
    'author' : 'Akshaya',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}