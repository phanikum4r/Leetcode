from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        def bfs(row, col, idx):
            if idx == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[idx]:
                return False
            
            original_char = board[row][col]
            board[row][col] = '#'  # Mark as visited
            
            for dr, dc in directions:
                if bfs(row + dr, col + dc, idx + 1):
                    return True
            
            board[row][col] = original_char  # Revert back
            return False
        
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c, 0):
                    return True
        
        return False
