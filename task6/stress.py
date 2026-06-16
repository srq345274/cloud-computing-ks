import urllib.request
import threading

URL = "http://127.0.0.1:5000/api/ping"

def worker():
    for _ in range(1000):
        try:
            urllib.request.urlopen(URL, timeout=3).read()
        except:
            pass

threads = []

for _ in range(100):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("stress test finished")
