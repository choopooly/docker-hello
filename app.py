#!/usr/bin/env python

import cherrypy
import socket


class Hello(object):
    @cherrypy.expose
    def index(self):
        return "Hello, I'm %s :)" % (socket.gethostname())
    index.exposed = True

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 5000})

    cherrypy.quickstart(Hello(), '/')
