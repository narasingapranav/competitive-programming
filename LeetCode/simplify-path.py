class Solution:
    def simplifyPath(self, path: str) -> str:
        p=[i for i in path.split('/') if i!=""]
        st=[]
        for i in p:
            if i=='.':
                continue
            if i!='..':
                st.append(i)
            else:
                if st:
                    st.pop()
                else:
                    continue
        return '/'+'/'.join(st)