class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # as we want min initialize all to max
        dp=[float("inf")]*n
        # src -> src cost =0
        dp[src]=0
        # k stops
        for _ in range(k+1):
            temp=dp.copy()
            for st,en,cos in flights:
                # if min go to min path
                if dp[st]!=float("inf"):
                    temp[en]=min(temp[en],dp[st]+cos)
            dp=temp
        return dp[dst] if dp[dst] !=float("inf") else -1