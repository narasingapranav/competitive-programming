class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pc=0
        mc=0
        for i in nums:
            if i==0:
                mc=max(mc,pc)
                pc=0
            else:
                pc+=1
        mc=max(mc,pc)
        return mc