from handlers.base import BaseHandler

import logging

class MainHandler(BaseHandler):
	def get(self):
		self.render("main.html")

