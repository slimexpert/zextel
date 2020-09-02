import os
import sys

sys.path.append('/opt/site_zextel/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zextel.settings'
import django
django.setup()

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
