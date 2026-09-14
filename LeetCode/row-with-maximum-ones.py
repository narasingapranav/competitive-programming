class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ro=0
        mo=0
        mr=0
        for i in range(len(mat)):
            ro=sum(mat[i])
            if ro>mo:
                mr=i
                mo=ro
        return [mr,mo]