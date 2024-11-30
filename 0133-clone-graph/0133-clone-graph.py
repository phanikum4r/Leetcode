"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # return copy.deepcopy(node)
        self.visited = {}
        def clone(node):
            if not node:
                return node
            if node in self.visited:
                return self.visited[node]

            new = Node(node.val, [])
            self.visited[node] = new

            if node.neighbors:
                new.neighbors = [clone(i) for i in node.neighbors]

            return new
        return clone(node)