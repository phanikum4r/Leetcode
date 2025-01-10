class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxArea = 0
        dp = [[0, 0, 0] for _ in range(n)]
        for j in range(n):
            if matrix[0][j] == '1':
                dp[j] = [1, 1, 1]
                maxArea = 1
        for i in range(1, m):
            prev = dp[:]
            dp = [[0, 0, 0] for _ in range(n)]
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0:
                        dp[j] = [1, 1, 1]
                        maxArea = max(maxArea, 1)
                        continue
                    dp[j][1] += dp[j - 1][1] + 1
                    dp[j][2] += prev[j][2] + 1
                    diag = int(sqrt(prev[j-1][0]))
                    side = min(dp[j][1], dp[j][2], diag + 1)
                    dp[j][0] = side * side
                    if dp[j][0] > maxArea:
                        maxArea = dp[j][0]
                else:
                    dp[j] = [0, 0, 0]
        return maxArea