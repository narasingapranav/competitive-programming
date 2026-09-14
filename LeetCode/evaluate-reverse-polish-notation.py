class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        r=[]
        for i in tokens:
            if i not in '+*/-':
                r.append(int(i))
            else:
                b=r.pop()
                a=r.pop()
                if i=='+':
                    r.append(a+b)
                elif i=='-':
                    r.append(a-b)
                elif i=='*':
                    r.append(a*b)
                elif i=='/':
                    r.append(int(a/b))
        return r.pop()