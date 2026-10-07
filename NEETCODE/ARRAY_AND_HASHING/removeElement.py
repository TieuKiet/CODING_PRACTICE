class Solution:
    def removeElement(self, nums: list[int], val: int) -> list[int]:
        

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1

        k = 0
        for num in nums:
            if num != -1 and num != None:
                k += 1

        nums.sort(key=lambda x: x < 0)

        return k

nums=[3,2,2,3]
val=3
sol = Solution()
print(sol.removeElement(nums, val))