import urllib.request as request
from pytimer import Timer

@Timer(label="time url request")
def task(n):
    for _ in range(n):
        request.urlopen("https://httpbin.org/")

task(1)
