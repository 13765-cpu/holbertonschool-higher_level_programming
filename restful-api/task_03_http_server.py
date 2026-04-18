from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # 1. Ana səhifə handling
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. /status endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # 3. /data endpoint (JSON qaytarır)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            json_response = json.dumps(sample_data)
            self.wfile.write(json_response.encode('utf-8'))

        # 4. Error handling (404) - DÜZƏLİŞ BURADADIR
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Test çox vaxt dəqiq bu mətni gözləyir
            self.wfile.write(b"Not Found")

# Serveri başlatmaq üçün hissə
def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server {port} portunda isleyir...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dayandirildi.")
        httpd.server_close()

if __name__ == "__main__":
    run()
