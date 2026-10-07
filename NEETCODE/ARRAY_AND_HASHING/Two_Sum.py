class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        check = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in check:
                check[nums[i]] = i

            else:
                return [check[diff], i]
    
     