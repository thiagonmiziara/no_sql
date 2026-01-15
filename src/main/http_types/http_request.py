class HttpRequest:
    def __init__(self, method: str, url: str, headers: dict = None, body: dict = None):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body
