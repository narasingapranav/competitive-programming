import math
class Solution:
    def countutility(self,cX,cY,r,darts):
        count = 0
        for x, y in darts:
            if (x - cX) ** 2 + (y - cY) ** 2 <= r * r + 1e-7:
                count += 1
        return count
    def computeutility(self,darts,dart,r,maxdarts):
        n=len(darts)
        for i in range(360):
            if maxdarts==n:
                return n
            angle=math.radians(i)
            cX=dart[0]+ r * math.cos(angle)
            cY=dart[1]+ r * math.sin(angle)
            counter=self.countutility(cX,cY,r,darts)
            if counter>maxdarts:
                maxdarts=counter
        return maxdarts
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        maxdarts=0
        n=len(darts)
        for i in range(n):
            maxdarts=max(maxdarts,self.computeutility(darts, darts[i], r, maxdarts))
        return maxdarts