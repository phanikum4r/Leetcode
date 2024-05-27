class Solution:
    def longestPalindrome(self, s: str) -> str:
        m,i,j=0,0,0
        low=0
        high=len(s)
        while low<high-1:
            for (a,b) in [(low,low),(low,low+1)]:
                c=0
                while a>=0 and b<high and s[a]==s[b]:
                    a-=1
                    b+=1
                    if a+1==b-1:
                        c+=1
                    else:
                        c+=2  
                if c>m:
                    m=c
                    i=a+1
                    j=b-1
            low+=1
        return s[i:j+1]
                    