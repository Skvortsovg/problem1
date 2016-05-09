import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl

from multiprocessing import Process, Queue
import os
from time import sleep

class http_server:
    def __init__(self, queue):
        self.server = HTTPServer(('localhost', 4000), RequestHandler)
        self.server.queue = queue
        self.server.serve_forever()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        d = parse_qsl(urlparse(self.path).query)
        self.server.queue.put(d)
        print(d ," added")

class Listener(Process):
    def __init__(self, queue):
        super(Listener, self).__init__()
        self.queue = queue
        self.start()

    def run(self):
        self.server = http_server(self.queue)

class Worker(Process):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.queue = queue
        self.setDaemon(True)
        self.start()

    def run(self):
        while True:
            try:    
                job = self.queue.get_nowait()
                sleep(int(job[0][1]))
                print(job, "_______")
                self.queue.task_done()
            except:
        #       print(job, "_______")
                sleep(0.8)

class Main():
    def __init__(self):
        self.queue = Queue()
        self.threads_count = int(input("Thread_count = "))
        self.listener = Listener(self.queue)
        self.threads = []
        self.threads=[Worker(self.queue) for _ in range(self.threads_count)]

        
m=Main()

        
