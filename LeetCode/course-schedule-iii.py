import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key= lambda x:(x[1],x[0]))
        tt=0
        nc=0
        q=[]
        for d,ld in courses:
            tt+=d
            heapq.heappush(q,-d)
            if tt>ld:
                tt-= -heapq.heappop(q)
        return len(q)