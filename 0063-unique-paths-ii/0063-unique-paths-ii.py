class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        n = len(obstacleGrid[0])
        dp = [1]
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                dp.append(0)
            else:
                dp.append(dp[i-1])       
        for i in range(1, len(obstacleGrid)):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j>0:
                    dp[j] += dp[j-1]
        return dp[-1]