class MinStack:

    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x: int) -> None:
        curr_min = self.getMin()
        self.stack.append((x, min(curr_min, x)))

    def pop(self) -> None:
        if len(self.stack) == 1:
            return None
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 1:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 1:
            return float('inf')
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()