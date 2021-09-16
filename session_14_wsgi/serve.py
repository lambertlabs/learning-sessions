from http.server import HTTPServer, SimpleHTTPRequestHandler


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hi there")


if __name__ == '__main__':
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()
