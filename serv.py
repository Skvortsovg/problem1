import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
import queue
from urllib.parse import urlparse, parse_qsl

q = queue.Queue()


class RequestHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        d = parse_qsl(urlparse(self.path).query)
        global q
        # print(d)
        q.put(d)
        print(q.qsize)


def print_queue(q):
    print(q)

Serveraddr = ('localhost', 4000)
srvr = HTTPServer(Serveraddr, RequestHandler)
srvr.serve_forever()
print_queue(q)


