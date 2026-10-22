class Solution:

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # Nếu người nhẹ nhất + người nặng nhất <= limit, ghép cả 2 vào 1 thuyền
            if people[left] + people[right] <= limit:
                left += 1  # Người nhẹ nhất đã lên thuyền

            # Người nặng nhất luôn phải lên thuyền (đi 2 người hoặc đi 1 mình)
            right -= 1
            boats += 1

        return boats