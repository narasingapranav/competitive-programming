class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                graph[i].append([j,dist])
                graph[j].append([i,dist])
        totalcost=0
        visited=set()
        minheap=[(0,0)]
        n=len(points)
        while len(visited)<n:
            d,node=heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            totalcost+=d
            for nei,wei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minheap,(wei,nei))
        return totalcost