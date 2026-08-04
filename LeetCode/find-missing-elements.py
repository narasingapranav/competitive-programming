class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi,mx=min(nums),max(nums)
        res=[]
        for i in range(mi,mx+1):
            if i not in nums:
                res.append(i)
        return res