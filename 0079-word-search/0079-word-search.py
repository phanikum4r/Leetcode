class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        n = len(word)

        def dfs(x, y, idx):
            if x < 0 or x >= r or y < 0 or y >= c or board[x][y] != word[idx]:
                return False
            if idx==n-1:
                return True
            # Temporarily modify the board to mark this cell as visited
            temp, board[x][y] = board[x][y], '#'
            
            # Explore all four directions
            found = (dfs(x + 1, y, idx + 1) or
                     dfs(x - 1, y, idx + 1) or
                     dfs(x, y + 1, idx + 1) or
                     dfs(x, y - 1, idx + 1))
            
            # Restore the original value
            board[x][y] = temp
            
            return found

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
