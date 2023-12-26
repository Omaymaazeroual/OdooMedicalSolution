{
    'name': "Medical Solution",
    'version': '1.0',
    'depends': ['base', 'board'],
    'author': "GI3-GL",
    'category': 'Medical System',
    'summary': 'Comprehensive Medical Management System  ',
    'description': """
        Enhance healthcare efficiency with this comprehensive medical management solution. Seamlessly manage patient appointments, maintain accurate medical records, and optimize clinic or hospital operations. Simplify patient care and streamline medical workflows for healthcare professionals.
    """,

#     'images': ['static/description/Logo.png'],

    # Data files always loaded at installation
    'data': [
        'views/appointment.xml',
        'views/doctor.xml',
        'views/medicalfile.xml',
        'views/patient.xml',
        'views/prescription.xml',
        'views/consultation.xml',
        'security/security.xml',
        'views/patient_registration.xml',
        'views/appointments_registration.xml',
        'views/appointment__List_Doctor.xml',
        'views/view_patient_infos.xml',
        'views/user.xml',
    ],


    'installable': True,
    'application': True,
    'auto_install': False,
}
