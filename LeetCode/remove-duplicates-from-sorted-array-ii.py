class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=Counter(nums)
        l=[]
        for i in c:
            if c[i]<=2:
                l.extend([i]*c[i])
            else:
                l.extend([i]*2)
        for i in range(len(l)):
            nums[i]=l[i]
        return len(l)