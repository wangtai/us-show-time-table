import sae
from showics import wsgi

application = sae.create_wsgi_app(wsgi.application)
