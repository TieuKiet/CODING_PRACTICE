class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        nums = sorted(set(nums))
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
                if count > max_count:
                    max_count = count

            else:
                count = 1

        return max_count 

s = Solution()
print(s.longestConsecutive(nums=[9,1,4,7,3,-1,0,5,8,-1,6]))