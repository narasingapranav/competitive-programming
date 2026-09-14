class Solution:
    '''def slope(self,p1,p2):
        x1,y1=p1
        x2,y2=p2
        if abs(x2-x1) ==0:
            return 1
        return (y2-y1)/(x2-x1)'''
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <=2:
            return len(points)
        maxi=2
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                counter=2
                for k in range(j+1,len(points)):
                    s1=(points[j][1]-points[i][1] )* (points[k][0]-points[i][0])
                    s2=(points[k][1]-points[i][1]) * (points[j][0]-points[i][0])
                    if s1==s2:
                        counter+=1
                maxi=max(maxi,counter)
        return maxi