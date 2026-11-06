class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> List[int]:
        res = arr[:k]
        n= len(arr)
        if n == k:
            return arr
        
        for i in range(k, n):
            a= arr[i]
            b= res[0]

            if (abs(a - x) < abs(b - x)) or (abs(a - x) == abs(b - x) and a < b):
                res.append(a)
                res.pop(0)
        
        return res

s= Solution()
print(s.findClosestElements(arr=[1,2,3,4,5], k=4, x=3))