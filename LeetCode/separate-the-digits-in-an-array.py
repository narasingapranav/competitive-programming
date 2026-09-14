class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if i<9:
                res.append(i)
            else:
                s=str(i)
                for j in s:
                    res.append(int(j))
        return res