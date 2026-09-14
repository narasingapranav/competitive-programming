class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi=min(nums)
        ma=max(nums)
        a=[]
        for i in range(mi,ma+1):
            if i not in nums:
                a.append(i)
        return a