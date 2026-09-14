class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=[0]*len(nums)
        sf=[0]*len(nums)
        res=[0]*len(nums)
        pf[0]=sf[len(nums)-1]=1
        for i in range(1,len(nums)):
            pf[i]=pf[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            sf[i]=sf[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=pf[i]*sf[i]
        return res