class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        m={}
        for c in "qwertyuiop":
            m[c]=1
        for c in "asdfghjkl":
            m[c]=2
        for c in "zxcvbnm":
            m[c]=3
        ans=[]
        for w in words:
            l=w.lower()
            r=m[l[0]]
            if all(m[c]==r for c in l):
                ans.append(w)
        return ans