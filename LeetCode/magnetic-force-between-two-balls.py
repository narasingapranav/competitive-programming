import math
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def solve(dist):
            c=1
            last=position[0]
            for i in position[1:]:
                if i-last>=dist:
                    c+=1
                    last=i
                    if c==m:
                        return True
            return False
        position.sort()
        l=1
        h=position[-1]-position[0]
        while l<=h:
            mid=l+(h-l)//2
            if solve(mid):
                l=mid+1
            else:
                h=mid-1
        return h