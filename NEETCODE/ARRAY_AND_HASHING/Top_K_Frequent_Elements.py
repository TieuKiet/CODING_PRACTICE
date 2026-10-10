class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        check = dict.fromkeys(nums, 0)
        for num in nums:
            check[num] += 1
        
        res = []
        arr = sorted(check.items(), key=lambda x: -x[1])
        for i in range(k):
            res.append(arr[i][0])

       
        return res
        

s = Solution()
print(s.topKFrequent(nums=[1,1,2,3,3,3],k=2))