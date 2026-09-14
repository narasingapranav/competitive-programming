class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t=sum(nums)
        if t%2 !=0:
            return False
        tar=t//2
        p={0}
        for i in nums:
            n=set()
            for j in p:
                n.add(i+j)
            p|=n
        return tar in p