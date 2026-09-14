class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        curEnd=0
        far=0
        n=len(nums)
        for i in range(n-1):
            far=max(far,i+nums[i])
            if i==curEnd:
                jumps+=1
                curEnd=far
        return jumps