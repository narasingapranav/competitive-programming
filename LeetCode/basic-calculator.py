class Solution:
    def calculate(self, s: str) -> int:
        ans=0
        n=0
        sign=1
        st=[sign]
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="(":
                st.append(sign)
            elif i==")":
                st.pop()
            elif i=='+' or i=='-':
                ans+=sign*n
                sign=(1 if i=='+' else -1)*st[-1]
                n=0
        return ans+sign*n