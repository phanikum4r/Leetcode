class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if i<0 or j<0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
                return
            board[i][j] = "1"
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)

        for i in (0,len(board)-1):
            for j in range(0,len(board[0])):
                if board[i][j] == "O":    
                    dfs(i,j)
        for i in range(1,len(board)-1):
            for j in (0,len(board[0])-1):
                if board[i][j] == "O":
                    dfs(i,j)

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "1":
                    board[i][j] = "O"