import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q=[]
        m=[]
        for i in range(len(profits)):
            heapq.heappush(q,(capital[i],profits[i]))
        for _ in range(k):
            while q and q[0][0]<=w:
                heapq.heappush(m,-heapq.heappop(q)[1])
            if not m:
                break
            w+= -heapq.heappop(m)
        return w