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

webpage = "<!DOCTYPE html><html><head><title>metrics_exporter</title><style>body{width:35em;margin: 0 auto;font-family: Tahoma, Verdana, Arial, sans-serif;}.colortext{color: blue;color: blue; }</style></head><body><h1><div style=\"text-align:center;\">Welcome to the Metrics Exporter!</div></h1><p><div style=\"text-align:center;font-size:13px;\"><em>Phantasie ist wichtiger als Wissen. Wissen ist begrenzt, Phantasie aber umfa&#223t die ganze Welt.</em></div></p><p style=\"text-align:right;font-size:12px;\"><em>Albert Einstein.</em></p><p style=\"font-size:24px;\"><u>Current Configuration:</u></p><p style=\"font-size:16px;\">Push Gateway Host: <span class=\"colortext\"><em>" + str(
    PGW_HOST) + "</em></span></p><p style=\"font-size:16px;\">Push Gateway Port: <span class=\"colortext\"><em>" + str(
    PGW_PORT) + "</em></span></p><p style=\"font-size:16px;\">Push Gateway Job Name: <span class=\"colortext\"><em>" + str(
    PGW_JOB_NAME) + "</em></span></p><p style=\"font-size:16px;\">Push Gateway Label Name: <span class=\"colortext\"><em>" + str(
    PGW_LABEL_NAME) + "</em></span></p><p style=\"font-size:16px;\">Push Gateway Label Value: <span class=\"colortext\"><em>" + str(
    PGW_LABEL_VALUE) + "</em></span></p><p style=\"font-size:16px;\">Bootstrap Server: <span class=\"colortext\"><em>" + str(
    BOOTSTRAP_SERVER) + "</em></span></p><p style=\"font-size:16px;\">Kafka Topic: <span class=\"colortext\"><em>" + str(
    KAFKA_TOPIC) + "</em></span></p><p style=\"font-size:16px;\">Group ID: <span class=\"colortext\"><em>" + str(
    GROUP_ID) + "</em></span></p><p style=\"font-size:16px;\">Kafka Key: <span class=\"colortext\"><em>" + str(
    KAFKA_KEY) + "</em></span></p><p style=\"font-size:16px;\">Metric Name: <span class=\"colortext\"><em>" + str(
    METRIC_NAME) + "</em></span></p><div style=\"text-align:center;font-size:12px;\"><p>Die_Zukunft&#169</p></div></body></html>"

hostName = '0.0.0.0'
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(webpage, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    webServer.serve_forever()