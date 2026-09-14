class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        st=[]
        for i in range(len(temp)):
            while st and temp[i]>temp[st[-1]]:
                idx=st.pop()
                res[idx]=i-idx
            st.append(i)
        return res