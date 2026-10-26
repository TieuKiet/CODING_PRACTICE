class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Lưu các index của các ngày

        for i in range(n):
            # Khi nhiệt độ ngày i ấm hơn ngày ở đỉnh stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            
            # Đưa ngày hiện tại vào stack đứng chờ
            stack.append(i)

        return res