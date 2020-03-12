import os
import sys
 
sys.path.append('/home/s/slimexpert/zextel/public_html/')
sys.path.append('/home/s/slimexpert/zextel/public_html/myenv/lib/python3.4/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zextel.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()