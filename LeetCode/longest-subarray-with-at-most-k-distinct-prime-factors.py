class Solution:
    def findfactors(self,num):
        s=set()
        d=2
        while d*d<=num:
            while num%d==0:
                s.add(d)
                num//=d
            d+=1
        if num>1:
            s.add(num)
        return s
    def longestSubarray(self, nums: list[int], k: int) -> int:
        res=0
        l=0
        dict={}
        for r in range(len(nums)):
            for i in self.findfactors(nums[r]):
                dict[i]=dict.get(i,0)+1
            while len(dict)>k:
                for i in self.findfactors(nums[l]):
                    dict[i]-=1
                    if dict[i]==0:
                        del dict[i]
                l+=1
            res=max(res,r-l+1)
        return res