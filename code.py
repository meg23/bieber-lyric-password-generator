
#!/usr/bin/env python

import re
import webapp2
import logging
import json
import os
import random
import random
import tswift
import requests
import requests_toolbelt.adapters.appengine

from bieber import Bieber
from normalizer import Normalizer
from datetime import datetime, date, time
from google.appengine.ext.webapp import template

requests_toolbelt.adapters.appengine.monkeypatch()

log = logging.getLogger('webapp')

class Main(webapp2.RequestHandler):

    def get(self):

        bieb = Bieber()

        song = re.sub("-", " ", bieb.getSong()._title).title()
        password = bieb.getPassword()

        template_values = {
            'password': password,
            'song': song,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', Main)], debug=True)

