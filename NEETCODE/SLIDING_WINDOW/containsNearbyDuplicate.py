class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True
            
            window.add(num)

            # Giữ kích thước cửa sổ không vượt quá k
            if len(window) > k:
                window.remove(nums[i - k])

        return False
s = Solution()
print(s.containsNearbyDuplicate(nums=[1,0,1,1], k=1))