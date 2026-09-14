class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=sorted(p)
        l=len(p)
        res=[]
        for i in range(len(s)-l+1):
            if sorted(s[i:i+l])==p:
                res.append(i)
        return res