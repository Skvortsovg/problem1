import queue
from  threading import Thread
from time import sleep


q = queue.Queue()
q.put(['5', '2'])
q.put(['6', '6'])
q.put(['5', '2'])
q.put(['4', '6'])
q.put(['13', '2'])
q.put(['0', '6'])
q.put(['5', '2'])
q.put(['6', '6'])
q.put(['5', '2'])
q.put(['4', '6'])
q.put(['13', '2'])
q.put(['0', '6'])


THREAD_COUNT = 5
workers = []


def worker():
    while True:
        line = q.get()
        sleeptime = int(line[0])
        sleep(sleeptime)
        q.task_done()

for _ in range(THREAD_COUNT):
    t = Thread(target=worker)
    workers.append(t)
    t.start()

q.join()