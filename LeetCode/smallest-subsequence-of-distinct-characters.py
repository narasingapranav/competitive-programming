class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq=Counter(s)
        seen=set()
        st=[]
        for i in s:
            freq[i]-=1
            if i in seen: 
                continue
            while st and st[-1]>i and freq[st[-1]]:
                seen.remove(st.pop())
            st.append(i)
            seen.add(i)
        return "".join(st)
        