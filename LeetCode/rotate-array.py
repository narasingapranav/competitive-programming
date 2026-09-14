class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        nums[:]=nums[(n-k):]+nums[:(n-k)]
        """
        Do not return anything, modify nums in-place instead.
        """
        