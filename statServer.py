#!/usr/bin/python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

server_address = ('0.0.0.0', 8081)    
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
os.chdir('/home/ubuntu/public_html')  # optional
print('Running server...')
httpd.serve_forever()
