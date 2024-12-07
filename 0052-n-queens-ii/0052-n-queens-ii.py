class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        chess = [[0 for _ in range(n)] for _ in range(n)]
        def backtrack(grid, idx, prev_pos):
            for i in range(n):
                if idx != 0 and (i==prev_pos-1 or i==prev_pos or i==prev_pos+1):
                    continue
                r, c = idx, i
                while r and c:
                    if grid[r-1][c-1] == 1:
                        break
                    r-=1
                    c-=1
                if r and c:
                    continue
                r, c = idx, i
                while r and c!=n-1:
                    if grid[r-1][c+1] == 1:
                        break
                    r-=1
                    c+=1
                if r and c!=n-1:
                    continue
                r = idx
                while r:
                    if grid[r-1][i] == 1:
                        break
                    r-=1
                if r:
                    continue
                if idx == n-1:
                    self.result += 1
                else:
                    grid[idx][i] = 1
                    backtrack(grid, idx + 1, i)
                    grid[idx][i] = 0
        backtrack(chess, 0, 0)
        return self.result