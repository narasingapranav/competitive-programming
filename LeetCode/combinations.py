from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a=[i for i in range(1,n+1)]
        c=combinations(a,k)
        l=[]
        for i in c:
            l.append(i)
        return l