class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def utility(op,cp,temp,res,n):
            if op+cp== 2*n:
                res.append(temp)
            if op<n:
                utility(op+1,cp,temp+'(',res,n)
            if cp<op:
                utility(op,cp+1,temp+')',res,n)
        op=0
        cp=0
        temp=""
        res=[]
        utility(op,cp,temp,res,n)
        return res