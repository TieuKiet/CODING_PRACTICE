class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = 0
        for i in range(-1,-n-1,-1):
            nums1[i] = nums2[idx]
            idx += 1
        
        nums1.sort()