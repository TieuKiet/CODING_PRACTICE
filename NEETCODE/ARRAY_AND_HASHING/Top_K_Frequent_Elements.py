class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # solution 1: using hash map and sort base on freq
        check = dict.fromkeys(nums, 0)
        for num in nums:
            check[num] += 1
        
        res = []
        arr = sorted(check.items(), key=lambda x: -x[1])
        for i in range(k):
            res.append(arr[i][0])

        return res

        # solution 2: Use the bucket sort algorithm
        '''
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Bước 2: Tạo mảng buckets với kích thước len(nums) + 1
        # Index của buckets là TẦN SUẤT xuất hiện
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Bước 3: Duyệt ngược từ tần suất cao nhất xuống thấp nhất O(N)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                # Đủ k phần tử thì dừng luôn
                if len(res) == k:
                    return res
                
        return res
        '''
        

s = Solution()
print(s.topKFrequent(nums=[1,1,2,3,3,3],k=2))