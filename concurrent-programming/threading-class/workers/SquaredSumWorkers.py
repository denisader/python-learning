import threading

class SquaredSumWorker(threading.Thread): # in this case it inherits from Thread
    def __init__(self, n):
        self._n = n # we have an internal parameter here (private)
        super().__init__() # all of the parent classes that this class inherits from will be initialized using this
        self.start() # start thread
    
    def _calculate_sum_squares(self): # internal method (reason for _))
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i ** 2
        
        print(sum_squares)

    def run(self):
        self._calculate_sum_squares()