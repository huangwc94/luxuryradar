import json
def analyze(image):
    id = 483932343
    return id

def connector():
    d = {
        "id": analyze("asdf")
    }
    return json.dumps(d)

def app(environ, start_response):

    if environ['REQUEST_METHOD'] == 'POST':
        data = json.dumps(str(environ))
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
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