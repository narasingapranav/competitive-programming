class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        def isi(num):
            try :
                int(num)
                return True
            except ValueError:
                return False
        for i in operations:
            if isi(i):
                    res.append(int(i))
            elif i=="C":
                res.pop()
            elif i=="D":
                res.append(2*res[-1])
            elif i=="+":
                res.append(res[-1]+res[-2])
        return sum(res)