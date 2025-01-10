class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        side = 0
        dp = [0 for _ in range(n)]
        for i in range(m):
            prev = dp[:]
            dp = [0 for _ in range(n)]
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0 or i == 0:
                        dp[j] = 1
                    else:
                        dp[j] = min(dp[j-1], prev[j], prev[j-1]) + 1
                    if dp[j] > side:
                        side = dp[j]
                else:
                    dp[j] = 0
        return side * side