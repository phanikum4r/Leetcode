class Solution:
    def numTilings(self, n: int) -> int:
        pmemo={}
        fmemo={}
        def p(n):
            if n==2:
                return 1
            if n in pmemo:
                return pmemo[n]
            pmemo[n] = (p(n-1)+f(n-2)) % 1000000007
            return pmemo[n]
        def f(n):
            if n==1:
                return 1
            elif n==2:
                return 2
            if n in fmemo:
                return fmemo[n]
            fmemo[n] = (f(n-1) + f(n-2) + 2 * p(n-1)) % 1000000007
            return fmemo[n]
        return f(n)