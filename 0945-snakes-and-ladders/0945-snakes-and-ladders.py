class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def findidx(cell):
            quot, rem = divmod(cell-1, n)
            return [n-quot-1,  n-rem-1] if quot%2 else [n-quot-1, rem]
        visited = set()
        q = deque([[1,0]])
        while q:
            cur, count = q.popleft()
            if cur == n**2:
                return count
            for nextloc in range(cur+1, min(n**2, cur + 6) + 1):
                r, c = findidx(nextloc)
                distance = board[r][c] if board[r][c]!=-1 else nextloc
                if distance not in visited:
                    visited.add(distance)
                    q.append([distance, count + 1])
        return -1