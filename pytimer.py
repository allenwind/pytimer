import time
import sys
from functools import wraps

class Timer:

    def __init__(self, label, func=time.perf_counter, output=sys.stdout):
        self.label = label
        self.output = output
        self._timeit = func
        self._elapsed = 0.0
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError("timer already started!")
        self._start = self._timeit()

    def stop(self):
        if self._start is None:
            raise RuntimeError("timer not started!")
        end = self._timeit()
        self._elapsed += end - self._start
        self._start = None

    def reset(self):
        self._elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    @property
    def elapsed(self):
        return self._elapsed

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.start()
            result = func(*args, **kwargs)
            self.stop()
            template = "{}\n{}.{} elapsed time:\n{:.3f}s"
            value = template.format(self.label, func.__module__, func.__name__, self._elapsed)
            print(value, end="\n\n", file=self.output)
            return result
        return wrapper

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

def timethis(label, timer=time.time, output=sys.stdout, callback=None):
    """
    带参数的计时器，支持指定计时器类型
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = timer()
            result = func(*args, **kwargs)
            end = timer()
            elapsed = end - start
            if callback is not None:
                callback(elapsed)
            template = "{}\n{}.{} elapsed time:\n{:.3f}s"
            value = template.format(label, func.__module__, func.__name__, elapsed)
            print(value, end="\n\n", file=output)
            return result
        return wrapper
    return decorate
