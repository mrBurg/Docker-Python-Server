"""Python server"""

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """Server entry point"""
    server_address = ("", 80)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):  # pylint: disable-msg=C0103
        """Get request"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write("<title>Простой HTTP-сервер.</title></head>".encode())
        self.wfile.write("<body>Был получен GET-запрос.</body></html>".encode())


run(handler_class=HttpGetHandler)
