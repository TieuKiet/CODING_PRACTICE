class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # Lượt 1: Tính prefix product từ trái sang phải trực tiếp vào res
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Lượt 2: Nhân dồn suffix product từ phải sang trái
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res


s = Solution()
print(s.productExceptSelf(nums = [1,2,4,6]))