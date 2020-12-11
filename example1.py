import urllib.request as request
from pytimer import Timer

def task(n):
    for _ in range(n):
        request.urlopen("https://httpbin.org/")


timer = Timer(label="request url")
with timer:
    task(5)

print(timer.elapsed)

# or

with Timer(label="request url") as timer:
    task(5)

print(timer.elapsed)
