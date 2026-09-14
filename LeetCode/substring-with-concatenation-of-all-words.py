class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen=len(words[0])
        l=0
        n=len(words)
        totallen=wordlen*n
        res=[]
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
        for i in range(wordlen):
            l=i
            c=0
            curr={}
            for r in range(i,len(s)-wordlen+1,wordlen):
                present=s[r:r+wordlen]
                if present in d:
                    curr[present]=curr.get(present,0)+1
                    c+=1
                    while curr[present]>d[present]:
                        lw=s[l:l+wordlen]
                        curr[lw]-=1
                        l+=wordlen
                        c-=1
                    if c==n:
                        res.append(l)
                else:
                    curr.clear()
                    c=0
                    l=r+wordlen
        return res