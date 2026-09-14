import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix=np.array(matrix)
        a=matrix.flatten()
        l,h=0,len(a)-1
        while l<=h:
            m=l+((h-l)//2)
            if a[m]==target: return True
            if a[m]<target: l=m+1
            else: h=m-1
        return False