class MinStack(object):

    def __init__(self):
        self.mainStack = list()
        self.minStack = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.mainStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        val = self.mainStack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop() 
        

    def top(self):
        """
        :rtype: int
        """
        return self.mainStack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()