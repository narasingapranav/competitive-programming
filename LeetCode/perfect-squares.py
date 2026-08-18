class Solution:
    def numSquares(self, n: int) -> int:
        def ps(sq,n,memo):
            if memo[n] !=-1:
                return memo[n]
            if n==0:
                return 0
            mx=n+1
            for i in sq:
                if i<=n:
                    mx=min(mx,1+ps(sq,n-i,memo))
            memo[n]=mx
            return mx
        sq=[]
        i=1
        memo=[-1]*(n+1)
        while i*i<=n:
            sq.append(i*i)
            i+=1
        return ps(sq,n,memo)