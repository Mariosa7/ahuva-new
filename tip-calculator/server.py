from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    port = 8000
    web_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.chdir(web_dir)
    print(f"Serving from directory: {os.getcwd()}")
    server_address = ("172.20.10.6", port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Serving on port {port}")
    httpd.serve_forever()
