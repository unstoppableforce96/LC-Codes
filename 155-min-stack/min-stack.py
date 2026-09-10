class MinStack:
    def __init__(self):
        self.st = []
        self.mnStack = []
    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mnStack:
            self.mnStack.append(value)
        else:
            self.mnStack.append(min(value, self.mnStack[-1]))
    def pop(self) -> None:
        self.mnStack.pop()
        return self.st.pop()
    def top(self) -> int:
        return self.st[-1]
    def getMin(self) -> int: # O(1) constant time
        return self.mnStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()