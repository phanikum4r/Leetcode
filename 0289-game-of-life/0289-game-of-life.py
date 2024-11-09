class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        result = []
        directions = [(1,0), (0,1), (1,1), (-1,-1), (-1,0), (0,-1), (-1,1), (1,-1)]
        def change(x,y):
            count = 0
            for dx,dy in directions:
                i=x+dx
                j=y+dy 
                if i>=m or i<0 or j>=n or j<0:
                    continue
                else:
                    count += board[i][j]
            return count

        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    if (change(i,j) < 2 or change(i,j) > 3):
                        result.append((i, j, 0))
                elif change(i,j)==3:
                    result.append((i, j, 1))
                
        for i,j,k in result:
            board[i][j] = k
