class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort(key=lambda x:(x[0],x[1]))
        res=0
        j=0
        for i in range(1,n+1):
            x=0
            while j<len(reservedSeats) and  reservedSeats[j][0]==i:
                x|= 1<<(10-reservedSeats[j][1])
                j+=1
            if x & 480 ==0 :
                if x&30 ==0:
                    res+=2
                else:
                    res+=1
            elif x&120==0:
                res+=1
            elif x&30==0:
                res+=1
            if j==len(reservedSeats):
                res+=(n-i)*2
                break
        return res
