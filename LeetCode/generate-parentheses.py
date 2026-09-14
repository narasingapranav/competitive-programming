class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def utility(op,cp,temp,res,n):
            if op+cp== 2*n:
                res.append(temp)
            if op<n:
                utility(op+1,cp,temp+'(',res,n)
            if cp<op:
                utility(op,cp+1,temp+')',res,n)
        res=[]
        utility(0,0,"",res,n)
        return res