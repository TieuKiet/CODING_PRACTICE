class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            
            stack.append(i)

        return res
    