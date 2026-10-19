class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k% len(nums) 
        t = nums[::-1]
        left = t[:k]
        right = t[k:]
        nums[:k] = left[::-1]
        nums[k:] = right[::-1]
