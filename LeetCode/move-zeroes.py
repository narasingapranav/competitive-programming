class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        j = 0
        for i in range(l):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        for i in range(j,l):
            nums[i] = 0
                
        """
        Do not return anything, modify nums in-place instead.
        """
        