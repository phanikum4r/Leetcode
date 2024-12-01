class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = {}
        def dfs(node):
            if node in self.visited:
                return self.visited[node]
            if node not in graph:
                self.visited[node]=1
                return 1
            self.visited[node] = 0
            res = 1
            for neighbor in graph[node]:
                res *= dfs(neighbor)
            self.visited[node] = res
            return res
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        for idx in graph:
            if not dfs(idx):
                return False
        return True