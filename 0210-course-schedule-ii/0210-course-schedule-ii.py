class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        res= []
        self.visited = {}
        def dfs(node):
            if node in self.visited:
                return self.visited[node]
            if node not in graph or not graph[node]:
                if node not in res:
                    res.append(node)
                return 1
            self.visited[node] = 0
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return 0
            res.append(node)
            self.visited[node] = 1
            graph[node] = []
            return 1
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        for idx in range(numCourses):
            if not dfs(idx):
                return []
        return res

        # visited = set()
        # def dfs(node):
        #     if node not in graph or not graph[node]:
        #         if node not in res:
        #             res.append(node)
        #         return 1
        #     if node in visited:
        #         return 0
        #     visited.add(node)
        #     for neighbor in graph[node]:
        #         if not dfs(neighbor):
        #             return 0
        #     res.append(node)
        #     graph[node] = []
        #     return 1