import subprocess
import sys
from cgi import parse_qs, escape
import base64
import luxuryradar

def application(environ, start_response):

    if environ['REQUEST_METHOD'] == 'POST':

        if environ['PATH_INFO'] == "/update":
            data = subprocess.check_output(["git","pull"],cwd="/home/huangwc94/luxuryradar")
            start_response("200 OK", [
                ("Content-Type", "text/plain"),
                ("Content-Length", str(len(data)))
            ])

            reload(luxuryradar)
        else:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            raw = environ['wsgi.input'].read(request_body_size)
            d = parse_qs(raw)

            baseData = d['encode_string']
            print baseData
            raw = base64.standard_b64decode(baseData[0])
            data = luxuryradar.identify(raw)

            start_response("200 OK", [
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(data)))
            ])
    elif environ['PATH_INFO'] == "/favicon.ico":
        with open('/home/huangwc94/luxuryradar/favicon.ico', mode='rb') as file:
            data = file.read()
        start_response("200 OK", [
            ("Content-Type", "image/x-icon"),
            ("Content-Length", str(len(data)))
        ])
    else:
        data = open('/home/huangwc94/luxuryradar/index.html').read()
        start_response("200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ])
    return iter([data])