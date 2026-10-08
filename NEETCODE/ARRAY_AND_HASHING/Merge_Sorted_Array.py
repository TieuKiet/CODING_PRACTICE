class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        check = dict.fromkeys(nums, 0)
        k = 0
        for i in range(len(nums)):
            if check[nums[i]] == 0:
                check[nums[i]] += 1
                k += 1
            else:
                nums[i] = 101
        
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 101:
                nums[idx], nums[i]= nums[i], nums[idx]
                idx += 1
        
        return k