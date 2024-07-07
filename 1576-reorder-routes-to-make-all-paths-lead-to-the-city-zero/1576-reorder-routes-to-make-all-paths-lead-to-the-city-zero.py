class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=defaultdict(list)
        directed=set()
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
            directed.add((a,b))
        res=0
        visited=[False]*n
        def dfs(city):
            nonlocal res
            visited[city]=True
            for neighbour in graph[city]:
                if not visited[neighbour]:
                    if (city,neighbour) in directed:
                        res+=1
                    dfs(neighbour)
        dfs(0)
        return res