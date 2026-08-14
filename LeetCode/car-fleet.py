class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(speed)
        car=[]
        for i,j in zip(position,speed):
            car.append((i,(target-i)/j))
        car.sort(key=lambda x:x[0],reverse=True)
        c=1
        t=car[0][1]
        for i in range(1,n):
            if car[i][1]>t:
                c+=1
                t=car[i][1]
        return c