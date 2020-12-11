import urllib.request as request
from pytimer import timethis

@timethis(label="time url request")
def task(n):
    for _ in range(n):
        request.urlopen("https://httpbin.org/")

task(1)

# change timer

from time import perf_counter

@timethis(label="time url request", timer=perf_counter)
def task(n):
    for _ in range(n):
        request.urlopen("https://httpbin.org/")

task(1)

# use callback

elapsed = 0
def set_value(t):
    global elapsed
    elapsed = t

@timethis(label="time url request", callback=set_value)
def task(n):
    for _ in range(n):
        request.urlopen("https://httpbin.org/")

task(1)

print(elapsed)

# use in a class


class Task:

    @timethis(label="time instance method")
    def urlopen1(self, url):
        request.urlopen(url)

    @classmethod
    @timethis(label="time class method")
    def urlopen2(self, url):
        request.urlopen(url)

    @staticmethod
    @timethis(label="time static method")
    def urlopen3(url):
        request.urlopen(url)

task = Task()
task.urlopen1("https://httpbin.org/")
task.urlopen2("https://httpbin.org/")
task.urlopen3("https://httpbin.org/")
