"""
WSGI config for blog_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_app.settings')

# ensure Django settings module is available before touching storage
from django.conf import settings
from django.utils.module_loading import import_string
from django.core.files.storage import default_storage

try:
    storage_cls = import_string(settings.DEFAULT_FILE_STORAGE)
    # only replace if needed (optional)
    if default_storage.__class__.__name__ != storage_cls.__name__:
        default_storage._wrapped = storage_cls()
except Exception as e:
    # log to stdout/stderr so you can see the problem during startup
    # (avoid crashing the WSGI process)
    import sys
    print("Could not set default_storage to", getattr(settings, 'DEFAULT_FILE_STORAGE', None), file=sys.stderr)
    print("Exception:", e, file=sys.stderr)

application = get_wsgi_application()

