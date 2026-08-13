class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD=10**9 +7
        res=0
        st=[]
        for i in range(len(arr)+1):
            while st and (i==len(arr) or arr[st[-1]]>=arr[i]):
                x=st.pop()
                lb=-1 if len(st)==0 else st[-1]
                ub=i
                c=((x-lb)*(ub-x))%MOD
                res=(res+arr[x]*c)%MOD
            st.append(i)
        return res