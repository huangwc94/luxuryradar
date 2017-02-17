import json
import cv2
import numpy as np
def analyze(data):
    a = np.fromstring(data,np.uint8)
    img = cv2.imdecode(a,cv2.IMREAD_COLOR)
    #s
    d = {
        "id": 483932343,
        "version":cv2.__version__,
        "img":a.size
    }
    return json.dumps(d)

def app(environ, start_response):

    if environ['REQUEST_METHOD'] == 'POST':
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        data = analyze(environ['wsgi.input'].read(request_body_size))

        start_response("200 OK", [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(data)))
        ])
    elif environ['PATH_INFO'] == "/favicon.ico":
        with open('favicon.ico', mode='rb') as file:
            data = file.read()
        start_response("200 OK", [
            ("Content-Type", "image/x-icon"),
            ("Content-Length", str(len(data)))
        ])
    else:
        data = open('index.html').read()
        start_response("200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ])
    return iter([data])