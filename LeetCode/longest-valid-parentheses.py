class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        st=[-1]
        cnt=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if len(st)==0:
                    st.append(i)
                else:
                    cnt=max(cnt,i-st[-1])
        return cnt