class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}  # { giá_trị : vị_trí }

        for i, num in enumerate(nums):
            # Nếu đã từng gặp num và khoảng cách <= k
            if num in seen and i - seen[num] <= k:
                return True
            
            # Cập nhật lại vị trí mới nhất của num
            seen[num] = i

        return False

s = Solution()
print(s.containsNearbyDuplicate(nums=[1,0,1,1], k=1))