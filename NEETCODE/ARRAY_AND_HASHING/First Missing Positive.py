class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        check = dict.fromkeys(nums, 0)
        for num in nums:
            check[num] += 1
        
        i = 1
        while i < max(nums):
            if i not in check:
                return i
            i+= 1
        
        if max(nums) < 0: return 1
        return max(nums) + 1