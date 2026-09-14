class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,te,tw=0,0,0
        if bills[0]!=5:
            return False
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                if f>=1:
                    f-=1
                    te+=1
                else:
                    return False
            else:
                if te>=1 and f>=1:
                    te-=1
                    f-=1
                    tw+=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True