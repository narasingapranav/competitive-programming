class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        a=None
        for i in nums:
            if c==0:
                a=i
                c=1
            elif i==a:
                c+=1
            else:
                c-=1
        return a

