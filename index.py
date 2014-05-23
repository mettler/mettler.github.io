#!/usr/bin/env python

''' Step 1: from the terminal, run: python thisfilename.py. Step 2: open browser to http://localhost:8080/. '''

from wsgiref.simple_server import make_server

cont = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
  </head>
  <body>Hi!
  </body>
</html>
'''

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [cont]

server = make_server('0.0.0.0', 8080, application)
server.serve_forever()