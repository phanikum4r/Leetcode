class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            st.append(i)
            while len(st)>1:
                if st[-2]<0 and st[-1]>0:
                    break
                if st[-1]*st[-2]>0:
                    break
                if st[-2]+st[-1]==0:
                    st.pop()
                    st.pop()
                elif abs(st[-2])>abs(st[-1]):
                    st.pop()
                else:
                    st[-2]=st[-1]
                    st.pop()
        return st