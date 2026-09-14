class Solution:
    def utility(self,op,cp,temp,res,n):
        if op+cp== 2*n:
            res.append(temp)
        if op<n:
            self.utility(op+1,cp,temp+'(',res,n)
        if cp<op:
            self.utility(op,cp+1,temp+')',res,n)
        return res
    def generateParenthesis(self, n: int) -> List[str]:
        op=0
        cp=0
        temp=""
        res=[]
        self.utility(op,cp,temp,res,n)
        return res