from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Served by backend: " + socket.gethostname()
        self.wfile.write(bytes(message, "utf8"))

PORT = 8080
server = HTTPServer(('', PORT), handler)
print("Server running...")
server.serve_forever()
