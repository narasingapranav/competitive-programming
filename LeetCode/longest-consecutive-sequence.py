class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        nums.sort()
        m=c=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                m=max(m,c)
            elif nums[i+1]==nums[i]+1:
                c+=1
            else:
                m=max(m,c)
                c=1
        m=max(m,c)     
        return m