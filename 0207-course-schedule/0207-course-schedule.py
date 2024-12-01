class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = {}
        def dfs(node):
            if node in self.visited:
                return self.visited[node]
            if node not in graph:
                return 1
            self.visited[node] = 0
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return 0
            self.visited[node] = 1
            graph[node] = []
            return 1
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        for idx in graph:
            if not dfs(idx):
                return False
        return True


        # visited = set()
        # def dfs(node):
        #     if node not in graph or not graph[node]:
        #         return 1
        #     if node in visited:
        #         return 0
        #     visited.add(node)
        #     for neighbor in graph[node]:
        #         if not dfs(neighbor):
        #             return 0
        #     graph[node] = []
        #     return 1