class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        i=0
        while i<len(s):
            if s[i] in "1234567890":
                a=s[i]
                while s[i+1] != '[':
                    a+=s[i+1]
                    i+=1
                st.append(int(a))
            elif s[i]==']':
                t=""
                while st[-1]!='[':
                    t=st.pop()+t
                st.pop()
                st[-1]=st[-1]*t
            else:
                st.append(s[i])
            i+=1
        return "".join(st)