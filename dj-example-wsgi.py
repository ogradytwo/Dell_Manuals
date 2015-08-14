# from pyany/ogradysocial, working on 22/07/15
#
  import os
  import sys
  path = '/Dj/150721'    # top level directory
  if path not in sys.path:
      sys.path.append(path)
  os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
  from django.core.wsgi import get_wsgi_application
  application = get_wsgi_application()
