class Solution:
    def sortArray(self, arr: list[int]) -> list[int]:
        def merge( left, right):
            result = []
            i = j = 0
    
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        if len(arr) <= 1: # BASE CASE
            return arr
    
        mid = len(arr) // 2
        left_half = self.sortArray(arr[:mid])
        right_half = self.sortArray(arr[mid:])
    
        return merge(self, left_half, right_half)

        