{
    'name': 'Demo Vendor WHT Engine',
    'version': '18.0.1.0',
    'summary': 'Vendor Bill Withholding Tax & Approval Flow',
    'author': 'Phurin Nararat',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/record_rule.xml',
        'views/account_move_view.xml',
        'report/report_vendor_bill.xml',
    ],
    'installable': True,
    'application': False,
}
