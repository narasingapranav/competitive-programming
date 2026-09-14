class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            while st and st[-1]>0 and i<0:
                if st[-1]<-i:
                    st.pop()
                    continue
                elif st[-1]==-i:
                    st.pop()
                break
            else:
                st.append(i)
        return st