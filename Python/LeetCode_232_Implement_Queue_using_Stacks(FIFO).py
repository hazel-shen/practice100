class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.temp_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        
        if not self.temp_stack: # temp_stack 為空的狀態
            while self.queue:
                self.temp_stack.append(self.queue.pop())

        return self.temp_stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.queue and not self.temp_stack:
            return self.queue[0]
        elif self.temp_stack:
            return self.temp_stack[-1]
        else:
            return None
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.queue and not self.temp_stack:
            return True
        else:
            return False
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()