class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        count = 0
        check = {0: 1}
        current_sum = 0
        for num in nums:

            current_sum += num

            count += check.get(current_sum - k, 0)
            
            check[current_sum] = check.get(current_sum, 0) + 1

        return count
s = Solution()
print(s.subarraySum( nums=[2,-1,1,2], k=2))
            

            

            