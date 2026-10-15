class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        check = dict.fromkeys(nums, 0)
        for num in nums:
            check[num] += 1
        
        res = []
        n = len(nums) / 3
        for key, value in check.items():
            if value > n:
                res.append(key)
        
        return res