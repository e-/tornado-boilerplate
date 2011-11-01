import tornado.web
import logging

class BaseHandler(tornado.web.RequestHandler):
	def __init__(self, *argc, **argkw):
		super(BaseHandler, self).__init__(*argc, **argkw)

