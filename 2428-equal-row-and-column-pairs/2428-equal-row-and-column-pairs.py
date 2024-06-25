class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        gridinverse=[]
        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append(grid[j][i])
            gridinverse.append(tuple(temp))
        grid=[tuple(row) for row in grid]
        res=0
        c1=Counter(gridinverse)
        c2=Counter(grid)
        for i in c1.keys():
            if i in c2.keys():
                res+=(c1[i]*c2[i])
        return res