class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp=0
        count=0
        for c in s:
            if c == 'b':
                count+=1
            else:
                dp=min(dp+1,count)
        return dp