import os

from django.core.wsgi import get_wsgi_application

## wsgi application using python default server

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()
