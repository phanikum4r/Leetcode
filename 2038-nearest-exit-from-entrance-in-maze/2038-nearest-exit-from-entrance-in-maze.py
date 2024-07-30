class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited=set()
        m=len(maze)
        n=len(maze[0])
        q=deque()
        entrance.append(0)
        q.append(tuple(entrance))
        while q:
            cur=q.popleft()
            if cur[0]==entrance[0] and cur[1]==entrance[1]:
                pass
            elif cur[0] in (0,m-1) or cur[1] in (0,n-1):
                return cur[2]
            if (cur[0],cur[1]) not in visited:
                visited.add((cur[0],cur[1]))
                if cur[1]+1<n and maze[cur[0]][cur[1]+1]=='.' and (cur[0],cur[1]+1) not in visited:
                    q.append((cur[0],cur[1]+1,cur[2]+1))
                if cur[1]-1>=0 and maze[cur[0]][cur[1]-1]=='.' and (cur[0],cur[1]-1) not in visited:
                    q.append((cur[0],cur[1]-1,cur[2]+1))
                if cur[0]-1>=0  and maze[cur[0]-1][cur[1]]=='.' and (cur[0]-1,cur[1]) not in visited:
                    q.append((cur[0]-1,cur[1],cur[2]+1))
                if cur[0]+1<m and maze[cur[0]+1][cur[1]]=='.' and (cur[0]+1,cur[1]) not in visited:
                    q.append((cur[0]+1,cur[1],cur[2]+1))
        return -1

                
