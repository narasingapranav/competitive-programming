class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create a graph
        g=defaultdict(list)
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                g[i].append((j,dist))
                g[j].append((i,dist))
        # total cost=0 , take a visited set
        tc=0
        vis=set()
        # create a min heap
        h=[(0,0)]
        n=len(points)
        while len(vis)<n:
            # pop the node and check if visited if not add distance and pudh neighbour heap
            dis,nod=heapq.heappop(h)
            if nod in vis:
                continue
            vis.add(nod)
            tc+=dis
            for nei,wei in g[nod]:
                if nei not in vis:
                    heapq.heappush(h,(wei,nei))
        return tc