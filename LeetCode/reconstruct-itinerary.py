import heapq
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        l=["JFK"]
        res=[]
        al=defaultdict(list)
        for s,e in tickets:
            heapq.heappush(al[s],e)
        while l:
            while al[l[-1]]:
                l.append(heapq.heappop(al[l[-1]]))
            res.append(l.pop())
        return res[::-1]