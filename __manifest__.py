# -*- coding: utf-8 -*-
{
    'name': 'school',
    'description': "This is module manager school and add subjects, students and teachers",
    'version': "1.0.0",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school_student_views.xml',
        'views/school_subject_views.xml',
        'views/school_teacher_views.xml',
        'views/school_menuitem.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}