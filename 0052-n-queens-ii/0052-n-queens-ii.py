class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                return 1
            solutions = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                if (col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals):
                    continue

                if row == n-1:
                    self.result += 1
                    continue

                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                backtrack(row + 1, diagonals, anti_diagonals, cols)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
            return solutions
            
        backtrack(0, set(), set(), set())
        return self.result

        # self.result = 0
        # chess = [[0 for _ in range(n)] for _ in range(n)]
        # def backtrack(grid, idx):
        #     for i in range(n):
        #         r, left, right = idx, i, i
        #         flag = 0
        #         while r:
        #             if r and left>0 and grid[r-1][left-1]:
        #                 flag = 1
        #                 break
        #             if r and right<n-1 and grid[r-1][right+1]:
        #                 flag = 1
        #                 break
        #             if r and grid[r-1][i]:
        #                 flag = 1
        #                 break
        #             r -= 1
        #             left -= 1
        #             right += 1
        #         if flag:
        #             continue
        #         if idx == n-1:
        #             self.result += 1
        #         else:
        #             grid[idx][i] = 1
        #             backtrack(grid, idx + 1)
        #             grid[idx][i] = 0
        # backtrack(chess, 0)
        # return self.result