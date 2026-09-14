class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[low]=nums[i]
                low+=1
        while low<len(nums):
            nums[low]=0
            low+=1