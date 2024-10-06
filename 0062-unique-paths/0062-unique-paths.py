class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo={}
        # def dp(i,j):
        #     if i==m-1 and j==n-1:
        #         return 1
        #     if i>m-1 or j>n-1:
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     memo[(i,j)] = dp(i+1,j)+dp(i,j+1)
        #     return memo[(i,j)]
        # return dp(0,0)
        
        res=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                res[i][j]=res[i-1][j]+res[i][j-1]
        return res[m-1][n-1]