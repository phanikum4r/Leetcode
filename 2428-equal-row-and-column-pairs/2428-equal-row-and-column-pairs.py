class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        gridinverse=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                gridinverse[j][i]=grid[i][j]
        for i in range(n):
            gridinverse[i]="".join(str(gridinverse[i]))
        for i in range(n):
            grid[i]="".join(str(grid[i]))
        res=0
        c=Counter(gridinverse)
        for i in grid:
            if i in c:
                res+=c[i]
        return res