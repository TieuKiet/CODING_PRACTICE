class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Thêm cột ảo có chiều cao 0 vào cuối để flush toàn bộ stack ở bước cuối
        heights.append(0)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            # Khi gặp cột thấp hơn cột ở đỉnh stack -> tính diện tích cho các cột trong stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                # Nếu stack rỗng, biên trái kéo dài tới đầu mảng (width = i)
                # Nếu stack không rỗng, biên trái là đỉnh stack hiện tại (i - stack[-1] - 1)
                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area