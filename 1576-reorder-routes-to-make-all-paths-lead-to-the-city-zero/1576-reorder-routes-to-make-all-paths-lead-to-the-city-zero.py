class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=defaultdict(dict)
        for a, b in connections:
            graph[a][b] = 1
            graph[b][a] = 0
        res=0
        visited=[False]*n
        q=deque([0])
        while q:
            city=q.popleft()
            visited[city]=True
            for neighbour,reverse in graph[city].items():
                if not visited[neighbour]:
                    res+=reverse
                    q.append(neighbour)
        return res