#!/usr/bin/python3
"""Simple HTTP API server."""

import http.server
import socketserver
import json


class Handler(http.server.SimpleHTTPRequestHandler):
    """Handle API GET routes."""

    def do_GET(self):
        """Serve responses for known endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", 'text/plain')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
