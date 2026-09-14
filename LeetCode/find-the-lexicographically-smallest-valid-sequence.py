class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n,m=len(word1),len(word2)
        last=[-1]*m
        i=n-1
        j=m-1
        while i>=0 and j>=0:
            if word1[i]==word2[j]:
                last[j]=i
                j-=1
            i-=1
        ans=[0]*m
        canchange=True
        j=0
        i=0
        while i<n and j<m:
            if word1[i]==word2[j]:
                ans[j]=i
                j+=1
            elif canchange and (j==m-1 or i<last[j+1]):
                ans[j]=i
                j+=1
                canchange=False
            if j==m:
                return ans
            i+=1
        return []