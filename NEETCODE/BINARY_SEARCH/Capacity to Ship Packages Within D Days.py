class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            day_needed = 1
            cur_load = 0
            mid = (l+r) // 2
            for w in weights:
                
                if cur_load + w <= mid:
                    cur_load += w
            
                else:
                    day_needed += 1
                    cur_load = w
            
            if day_needed <= days:
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1
        
        return res
        
        