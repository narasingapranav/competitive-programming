import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, st: List[List[int]]) -> int:
        heap=[]
        fuel=startFuel
        n=len(st)
        stopC=0
        i=0
        while fuel<target:
            while i<n and st[i][0]<=fuel:
                heapq.heappush(heap,-st[i][1])
                i+=1
            if not heap:
                return -1
            fuel+= -heapq.heappop(heap)
            stopC+=1
        return stopC