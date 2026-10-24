class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_min = [2**31]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefix_min.append( min(self.prefix_min[-1], val) )
        

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_min[-1]