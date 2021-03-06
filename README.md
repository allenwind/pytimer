# pytimer

在模型训练或数据处理中，常常涉及代码段的计时，这里给出优雅的计时器实现。


例子一，作为上下文管理器，

```python
import urllib.request as request
from pytimer import Timer

def task(n):
    for _ in range(n):
        request.urlopen("https://httpbin.org/")

with Timer(label="request url") as timer:
    task(5)

print(timer.elapsed)
```

例子二，作为装饰器，

```python
import urllib.request as request
from pytimer import Timer

@Timer(label="time url request")
def task(n):
    for _ in range(n):
        request.urlopen("https://httpbin.org/")

task(1)
```

例子三，在类中使用，

```python
import urllib.request as request
from pytimer import timethis

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
```
