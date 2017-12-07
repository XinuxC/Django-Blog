"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

'''
WSGI (Python Web Server Gateway Interface)
Python服务器网关接口
Python 应用与web服务器之间的接口
(只有实现了wsgi接口以后,web服务器才能识别Python网站,提供相应的服务,才能访问网站)
'''

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

application = get_wsgi_application()
