class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        st=[]
        i=0
        res=0
        while st or i<n:
            if i<n and (not st or heights[st[-1]]<=heights[i]):
                st.append(i)
                i+=1
            else:
                t=st.pop()
                h=heights[t]
                w= i if not st else i-st[-1]-1
                res=max(res,h*w)
        return res