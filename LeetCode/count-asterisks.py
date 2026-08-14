class Solution:
    def countAsterisks(self, s: str) -> int:
        r=s.split('|')
        ans=0
        for i in range(0,len(r),2):
            ans+=r[i].count('*')
        return ans