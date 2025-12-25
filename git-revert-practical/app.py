# temp_server.py
# A simple temporary HTTP server

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as server:
    print(f"Server running on port {PORT}")
    server.serve_forever()
