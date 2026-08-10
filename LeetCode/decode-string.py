class Solution:
    def decodeString(self, s: str) -> str:
        num=[]
        st=[]
        i=0
        res=""
        n=len(s)
        while i<n:
            if s[i].isdigit():
                x=0
                while i<n and s[i].isdigit():
                    x=x*10+int(s[i])
                    i+=1
                num.append(x)
                continue
            elif s[i]=='[':
                st.append("")
            elif s[i].isalpha():
                if st:
                    st[-1]+=s[i]
                else:
                    res+=s[i]
            else:
                popped=st.pop()
                popnum=num.pop()
                if st:
                    st[-1]+=popped*popnum
                else:
                    res+=popped*popnum
            i+=1
        return res