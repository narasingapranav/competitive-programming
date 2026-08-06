class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalin(s):
            return s==s[::-1]
        res=[]
        def backtrack(s,st=0,cur=None):
            if st>=len(s):
                res.append(cur[:])
                return
            if cur==None:
                cur=[]
            for i in range(st+1,len(s)+1):
                a=s[st:i]
                if ispalin(a):
                    cur.append(a)
                    backtrack(s,i,cur)
                    cur.pop()
        backtrack(s)
        return res