class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p=nums[i]*nums[j]
                d[p]=d.get(p,0)+1
        ans=0
        for c in d.values():
            ans+=8*c*(c-1)//2
        return ans