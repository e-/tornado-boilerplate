# -*- coding: utf8 -*-

import tornado.ioloop
import tornado.httpserver
import tornado.web

from tornado.options import options

from routes import routes
from settings import settings

class Application(tornado.web.Application):
	def __init__(self):
		tornado.web.Application.__init__(self, routes, **settings)
		

def main():
	tornado.options.parse_command_line()
	app = Application()
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()

