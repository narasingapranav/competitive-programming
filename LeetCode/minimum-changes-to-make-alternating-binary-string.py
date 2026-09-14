class Solution:
    def minOperations(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            if int(s[i]) != i%2:
                res+=1
        return min(res,len(s)-res)