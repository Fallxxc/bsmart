DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "HOST": "10.2.0.17",
        "PORT": 5432,
        "NAME": "alerte",
        "USER": "attack",
        "PASSWORD": "attack",
        'CONN_MAX_AGE': 0
    },
}

DEBUG = False
ALLOWED_HOSTS = ["10.2.0.16", "b-smarttools.com", "www.b-smarttools.com"]

SECRET_KEY = "qliv-rs0nz3z0ccut(ie0$di0bm011-53y@q^u$^v9@kkpodesr"
