class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbour, edge in enumerate(isConnected[city]):
                if not visited[neighbour] and edge:
                    visited[neighbour]=True
                    dfs(neighbour)
        n=len(isConnected)
        visited=[False]*n
        res=0
        for i in range(n):
            if not visited[i]:
                visited[i]=True
                res+=1
                dfs(i)
        return res