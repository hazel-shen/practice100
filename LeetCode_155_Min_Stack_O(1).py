class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

        self.stack.append(val)
        return self.stack
        

    def pop(self):
        """
        :rtype: None
        """

        try:
            pop_value = self.stack.pop()
            if self.min_stack and pop_value == self.min_stack[-1]:
                self.min_stack.pop()
            return pop_value
        except IndexError:
            print("Can't pop: stack is empty.")
            return None

    def top(self):
        """
        :rtype: int
        """
        try:
            return self.stack[-1]
        except IndexError:
            print("Can't get top: stack is empty.")
            return None
        
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

s = MinStack()
s.push(5)
s.push(3)
s.push(4)
print(s.getMin())  # 期待 3
s.pop()
print(s.getMin())  # 期待 3
s.pop()
print(s.getMin())  # 期待 5
