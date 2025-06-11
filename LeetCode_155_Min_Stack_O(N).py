class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        return self.stack
        

    def pop(self):
        """
        :rtype: None
        """
        
        try:
            return self.stack.pop()
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
        if not self.stack:
            return None

        test_n = self.stack[0]
        for n in self.stack:
            if test_n > n:
                test_n = n
        return test_n
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minstack = MinStack()
minstack.push(42)
print(minstack.getMin())  # ➤ 預期 42
print(minstack.top())     # ➤ 預期 42
minstack.pop()
# 接下來 top() 或 getMin() 都會壞掉（你要想一下怎麼處理）
