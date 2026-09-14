class Solution:
    def find(self,s):
        count=1
        res=""
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                res+=str(count)+s[i-1]
                count=1
        res+=str(count)+s[-1]
        return res
    def countAndSay(self, n: int) -> str:
        res="1"
        for i in range(1,n):
            res=self.find(res)
        return res
