class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        check = dict.fromkeys(nums, 0)
        n = len(nums) / 2
        for num in nums:
            check[num] += 1

        for key, value in check.items():
            if value > n:
                return key


sol = Solution()
print(sol.majorityElement(nums = [5,5,1,1,1,5,5]))