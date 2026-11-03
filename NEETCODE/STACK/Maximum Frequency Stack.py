class FreqStack:

    def __init__(self):
        self.arr = []
        self.count = {}

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.count[val] = self.count.get(val, 0) + 1


    def pop(self) -> int:
        max_count = 0
        for value in self.count.values():
            if value >= max_count:
                max_count = value

        for i in range(len(self.arr) - 1, -1, -1):
            if self.count[self.arr[i]] == max_count:
                self.count[self.arr[i]] -= 1
                res = self.arr.pop(i)
                
                return res
        
        return self.arr.pop()


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()