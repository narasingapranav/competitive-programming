class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            s=str(i)
            for j in s:
                res.append(int(j))
        return res