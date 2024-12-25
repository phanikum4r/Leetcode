class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # for i in range(1, len(grid)):
        #     grid[i][0] += grid[i-1][0]
        # for j in range(1, len(grid[0])):
        #     grid[0][j] += grid[0][j-1]
        # for i in range(1, len(grid)):
        #     for j in range(1,len(grid[0])):
        #         grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        # return grid[-1][-1]

        m, n = len(grid), len(grid[0])
        dp = [grid[0][0]]
        for i in range(1, n):
            dp.append(grid[0][i]+dp[i-1])
        for i in range(1, m):
            for j in range(n):
                if not j:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]