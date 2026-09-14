from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a=[i for i in range(1,n+1)]
        p=permutations(a)
        m=[]
        for i in p:
            s=""
            for j in i:
                s+=str(j)
            m.append(s)
        return m[k-1]