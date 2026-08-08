class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        s=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                s-=1
            else:
                s+=1
            if s in d:
                ans=max(i-d[s],ans)
            else:
                d[s]=i
        return ans