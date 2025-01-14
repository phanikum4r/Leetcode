class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr=[['.' for j in range(n)] for i in range(n)]
        result = []
        def backtrack(row, cols, diagnols, antidiagnols, arr):
            if row == n:
                return
            for col in range(n):
                diagnol = row - col
                anti = row + col

                if col in cols or diagnol in diagnols or anti in antidiagnols:
                    continue
                
                arr[row][col] = 'Q'
                if row == n-1:
                    temp = []
                    for r in arr:
                        temp.append(''.join(r))
                    result.append(temp)
                cols.add(col)
                diagnols.add(diagnol)
                antidiagnols.add(anti)
                backtrack(row + 1, cols, diagnols, antidiagnols, arr)
                cols.remove(col)
                diagnols.remove(diagnol)
                antidiagnols.remove(anti)
                arr[row][col] = '.'
        backtrack(0, set(), set(), set(), arr)
        return result