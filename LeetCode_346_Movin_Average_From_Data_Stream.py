from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.queue = deque()
        self.size = size
        self.sum = 0.0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
   
        self.queue.append(val)
        self.sum += val

        if len(self.queue) > self.size: # 如果 queue > 提供的 window 
            self.sum -= self.queue.popleft()
           
        result = self.sum / len(self.queue)
        print(result)
        return result
        

m = MovingAverage(2)
m.next(-1)  # -1.0
m.next(2)   # 0.5
m.next(3)   # 2.5
m.next(4)   # 3.5