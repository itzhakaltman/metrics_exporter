#!/usr/bin/env python3

import http.server
import random
from prometheus_client import start_http_server, Counter

REQUEST_COUNT = Counter('app_requests_count', 'total app http request count', ['app_name', 'endpoint'])
RANDOM_COUNT = Counter('app_random_count', 'increment counter by random value')

APP_PORT = 8080
METRICS_PORT = 8090

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        REQUEST_COUNT.labels('prom_python_app', self.path).inc()
        random_val = random.random() * 10
        RANDOM_COUNT.inc(random_val)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<!DOCTYPE html><html><head><title>metrics_generator</title><style>body{width:30em;margin: 0 auto;font-family: Tahoma, Verdana, Arial, sans-serif;}</style></head><body><h1>Welcome to the Prometheus Metrics Generator!</h1><p><em>Phantasie ist wichtiger als Wissen. Wissen ist begrenzt, Phantasie aber umfa&#223t die ganze Welt.</em></p><p><em>Albert Einstein.</em></p><p>Die Zukunft&#169</p></body></html>","utf-8"))

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('0.0.0.0', APP_PORT), HandleRequests)
    server.serve_forever()