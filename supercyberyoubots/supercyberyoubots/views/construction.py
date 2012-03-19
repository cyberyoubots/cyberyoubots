# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
import os
from google.appengine.ext.webapp import template


class UnderConstructionHandler(webapp.RequestHandler):
    def get(self):
        _get_context = {}
        path = os.path.join(os.path.dirname(__file__), 'templates', 'under_construction.html')
        self.response.out.write(template.render(path, _get_context))
        return 