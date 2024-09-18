class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nr=len(grid)
        nc=len(grid[0])
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        result=0
        count=0
        v=0
        q=deque()             
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    count+=1
        while q:
            x,y,v=q.popleft()
            result=max(result,v)
            for (r,c) in directions:
                if 0<=x+r<nr and 0<=y+c<nc and grid[x+r][y+c]==1:
                    grid[x+r][y+c]=0
                    count-=1
                    q.append((x+r,y+c,v+1))
                if 0<x+r<nr and 0<y+c<nc and grid[x+r][y+c]==2:
                    grid[x+r][y+c]=0
                    q.append((x+r,y+c,0))
        return -1 if count else result