class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        ms={}
        mt={}
        for i,j in zip(s,t):
            if i in ms and ms[i]!=j:
                return False
            if j in mt and mt[j]!=i:
                return False
            ms[i]=j
            mt[j]=i
        return True