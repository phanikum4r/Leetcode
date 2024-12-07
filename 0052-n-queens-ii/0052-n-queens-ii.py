class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        chess = [[0 for _ in range(n)] for _ in range(n)]
        def backtrack(grid, idx):
            for i in range(n):
                r, left, right = idx, i, i
                flag = 0
                while r:
                    if r and left>0 and grid[r-1][left-1]:
                        flag = 1
                        break
                    if r and right<n-1 and grid[r-1][right+1]:
                        flag = 1
                        break
                    if r and grid[r-1][i]:
                        flag = 1
                        break
                    r -= 1
                    left -= 1
                    right += 1
                if flag:
                    continue
                if idx == n-1:
                    self.result += 1
                else:
                    grid[idx][i] = 1
                    backtrack(grid, idx + 1)
                    grid[idx][i] = 0
        backtrack(chess, 0)
        return self.result