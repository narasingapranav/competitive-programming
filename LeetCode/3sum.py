class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        if nums[0]>0 :
            return res
        n=len(nums)
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(n-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-1):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                k=-(nums[i]+nums[j])
                if k in d and d[k]>j:
                    res.append([nums[i],nums[j],k])
        return res