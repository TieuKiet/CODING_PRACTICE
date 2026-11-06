from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # Lưu chỉ số (index) của các phần tử
        res = []

        for i, val in enumerate(nums):
            # 1. Loại bỏ index đã trượt ra khỏi cửa sổ (bên trái)
            if q and q[0] < i - k + 1:
                q.popleft()

            # 2. Loại bỏ các phần tử nhỏ hơn hoặc bằng val ở cuối deque (bên phải)
            while q and nums[q[-1]] <= val:
                q.pop()

            # 3. Thêm index hiện tại vào deque
            q.append(i)

            # 4. Khi cửa sổ đã đủ kích thước k, lấy max (chính là nums[q[0]])
            if i >= k - 1:
                res.append(nums[q[0]])

        return res