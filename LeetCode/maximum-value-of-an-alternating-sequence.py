class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        # res=[s]
        # if n>1:
        #     ans=s+m
        #     res.append(ans)
        #     i=2
        #     while i<n:
        #         if i&1:
        #             res.append(res[i-1]+m)
        #         else:
        #             res.append(res[i-1]-1)
        #         i+=1
        #     return max(res)
        pk=n//2
        return s+pk*m-(pk-1)