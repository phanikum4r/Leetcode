class Solution:
    def numTilings(self, n: int) -> int:
        # pmemo={}
        # fmemo={}
        # def p(n):
        #     if n==2:
        #         return 1
        #     if n in pmemo:
        #         return pmemo[n]
        #     pmemo[n] = (p(n-1)+f(n-2)) % 1000000007
        #     return pmemo[n]
        # def f(n):
        #     if n==1:
        #         return 1
        #     elif n==2:
        #         return 2
        #     if n in fmemo:
        #         return fmemo[n]
        #     fmemo[n] = (f(n-1) + f(n-2) + 2 * p(n-1)) % 1000000007
        #     return fmemo[n]
        # return f(n)

        f1,f2,p1,p2=1,2,0,1
        fn=0
        if n==1:
            return f1
        elif n==2:
            return f2
        for i in range(3,n+1):
            fn=(f2+f1+(2*p2)) % 1000000007
            p1=p2
            p2+=f1
            f1=f2
            f2=fn   
        return fn