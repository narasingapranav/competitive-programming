class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            d={}
            i=0
            ans=0
            n=len(nums)
            for j in range(n):
                d[nums[j]]=d.get(nums[j],0)+1
                while len(d)>k:
                    d[nums[i]]-=1
                    if d[nums[i]]==0:
                        del d[nums[i]]
                    i+=1
                ans+=j-i+1
            return ans
        return atmost(k)-atmost(k-1)
