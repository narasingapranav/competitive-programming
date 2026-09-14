class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        res=[]
        prev=lower-1
        for i in nums:
            if i<lower or i>upper:
                continue
            if i>prev+1:
                res.append((prev+1,i-1))
            prev=i
        if prev<upper:
            res.append((prev+1,upper))
        return res