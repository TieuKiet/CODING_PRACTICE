class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        if nums[right] < target:
            return len(nums) 
        
        if nums[left] > target:
            return 0
        
        # nums[mid] sao cho nums[left] < nums[mid] < nums[right] với điều kiện right = left + 1
        while right != left + 1 and left < right:
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid 
            
            elif nums[mid] > target:
                right = mid
            
            mid = (left + right) // 2
        
        return right