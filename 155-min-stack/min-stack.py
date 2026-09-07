class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 999999999999999999
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if value < self.min:
            self.min = value

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            self.min = min(self.stack) if self.stack else 999999999999999999

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()