
import time
import requests

class Timer:
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.duration = None
    
    def start(self):
        self.startTime = time.perf_counter()
        self.endTime = None
        self.duration = None
    
    def end(self):
        if self.startTime == None:
            return None
        self.endTime = time.perf_counter()
        self.duration = self.endTime - self.startTime
        return self.duration
    
    def elapsed(self):
        return time.perf_counter() - self.startTime if self.startTime else None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self):
        self.exit()
    