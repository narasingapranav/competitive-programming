class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ro=0
        mo=0
        mr=0
        for i in range(len(mat)):
            # ro=sum(mat[i])
            c=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    c+=1
            if c>mo:
                mr=i
                mo=c
        return [mr,mo]