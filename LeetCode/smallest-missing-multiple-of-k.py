class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        m=max(nums)
        for i in range(k,m+k+1,k):
            if i not in s:
                return i