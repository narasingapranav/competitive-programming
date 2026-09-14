class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        a=0
        m=0
        while l<r:
            a=min(height[l],height[r])*(r-l)
            m=max(a,m)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m
                
