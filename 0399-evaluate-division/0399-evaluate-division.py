class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        for (a,b),val in zip(equations,values):
            graph[a].append([b,val])
            graph[b].append([a,1/val])
        def dfs(a,b,v):
            if a not in visited:
                visited.add(a)
                for (neighbor,val) in graph[a]:
                    t=v*val
                    if neighbor==b:
                        self.prod=t
                    dfs(neighbor,b,t) 
            
        res=[]
        self.prod=-1.0
        for (a,b) in queries:
            visited=set()
            if (a not in graph) or (b not in graph):
                res.append(-1.0)
            elif a==b:
                res.append(float(1))
            else:
                self.prod=-1.0
                dfs(a,b,1.0)
                res.append(self.prod)
        return res