from public.models import helpers

contacts = [{
        'src': '{scheme}://{host}/static/public/img/cv3.png',
        'content': 'resume',
        'url': 'https://www.visualcv.com/arcbze7iaos/pdf',
        'col': 'col-lg-4'
    }, {
        'src': '{scheme}://{host}/static/public/img/phone.png',
        'content': '+359898633813',
        'col': 'col-lg-4'
    }, {
        'src': '{scheme}://{host}/static/public/img/envelope.png',
        'content': 'angelovradostin@gmail.com',
        'col': 'col-lg-4'
    }, {
        'src': '{scheme}://{host}/static/public/img/linkedin.png',
        'content': 'LinkedIn',
        'url': 'https://www.linkedin.com/in/radostin-angelov-399627101/',
        'col': 'col-lg-4'
    }, {
        'src': '{scheme}://{host}/static/public/img/wordpress.png',
        'content': 'resolvecs.wordpress.com/',
        'url': 'https://resolvecs.wordpress.com/',
        'col': 'col-lg-4'
    }, {
        'src': '{scheme}://{host}/static/public/img/globe.png',
        'content': 'nelfurion.com/',
        'url': 'http://nelfurion.com/',
        'col': 'col-lg-4'
    },
]

def get_models(options):
    """ options: {'host': hostname} """
    return {
        'contacts': helpers.format_models(contacts, options),
    }
