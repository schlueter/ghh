from ghh.handler import Handler


class WSGIApp:

    def __init__(self, config_file=None):
        self.handler = Handler(config_file)

    def __call__(self, environ, start_response):
        environ = environ
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [b"Hello world!\n"]
