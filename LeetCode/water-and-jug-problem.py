class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target<=x+y and target % self.gcd(x,y)==0:
            return True
        return False