# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.result = {}
        def trav(node, level):
            if node:
                self.result.setdefault(level, []).append(node.val)
                trav(node.left, level+1)
                trav(node.right, level+1)
        trav(root, 0)
        for key, values in self.result.items():
            self.result[key] = sum(values)/len(values)
        return list(self.result.values())