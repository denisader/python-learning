import threading
import time

class SleepyWorker(threading.Thread):
    def __init__(self, seconds, **kwargs): # collects extra keyword arguments to forward to the parent Thread.__init__
        # without kvargs, you would have to explicitly name every argument
        super().__init__(**kwargs)
        self._seconds = seconds
        self.start()
    
    def _sleep_a_little(self):
        time.sleep(self._seconds)
    
    def run(self):
        self._sleep_a_little()