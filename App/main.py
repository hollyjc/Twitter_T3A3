import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def try_app():
    print("time to marry rich") 

#######3