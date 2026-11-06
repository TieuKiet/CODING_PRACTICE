class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = 1000000001
        n = len(nums)
        left = 0
        right = 0
        prefix_sum = 0

        while right < n:
            
            if prefix_sum + nums[right] < target:
                prefix_sum += nums[right]
                right += 1

            
            elif prefix_sum + nums[right] >= target:
                prefix_sum -= nums[left]
                min_len = min(min_len, right - left + 1)
                left += 1
        
        if min_len == 1000000001:
            return 0
        
        return min_len

s= Solution()
print(s.minSubArrayLen(target = 5, nums = [1,2,1]))