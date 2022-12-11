# -*- coding: utf-8 -*-
{
    'name': "VideoClub",

    'summary': """
        Módulos de gestión de peliculas""",

    'description': """
        Ejemplo de funcionalidad para un módulo encargado de gestionar peliculas.
        Mostrar listados, dar de alta, baja ..etc. 
    """,
    'application': True,
    'author': "José Ramón López",
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/videoclub.xml'
    ],
}
