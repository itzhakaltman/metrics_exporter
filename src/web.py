#!/usr/bin/env python3


from http.server import BaseHTTPRequestHandler, HTTPServer

from config import PGW_HOST
from config import PGW_PORT
from config import PGW_JOB_NAME
from config import PGW_LABEL_NAME
from config import PGW_LABEL_VALUE
from config import BOOTSTRAP_SERVER
from config import KAFKA_TOPIC
from config import GROUP_ID
from config import KAFKA_KEY
from config import METRIC_NAME


# c10 = 'PGW HOST' + ': ' + str(PGW_HOST) + '\n' + 'PGW PORT' + ': ' + str(PGW_PORT) + '\n' + 'BOOTSTRAP SERVER' + ': ' + str(BOOTSTRAP_SERVER) + '\n' + 'TOPIC' + ': ' + str(KAFKA_TOPIC) + '\n' + 'GROUP ID' + ': ' + str(GROUP_ID) + '\n' + 'KEY' + ': ' + str(KAFKA_KEY) + '\n' + 'METRIC NAME' + ': ' + str(METRIC_NAME) + '\n' + 'JOB NAME' + ': ' + str(PGW_JOB_NAME) + '\n' + 'LABEL NAME' + ': ' + str(PGW_LABEL_NAME) + '\n' + 'LABEL VALUE' + ': ' + str(PGW_LABEL_VALUE)
webpage = "<!DOCTYPE html><html><head><title>metrics_exporter</title><style>body{width:30em;margin: 0 auto;font-family: Tahoma, Verdana, Arial, sans-serif;}</style></head><body><h1>Welcome to the Metrics Exporter!</h1><p><em>Phantasie ist wichtiger als Wissen. Wissen ist begrenzt, Phantasie aber umfa&#223t die ganze Welt.</em></p><p><em>Albert Einstein.</em></p><p>Die Zukunft&#169</p></body></html>"

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(webpage,"utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
