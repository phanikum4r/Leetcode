# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = {}
        def trav(node, level):
            if node:
                self.result.setdefault(level, []).append(node.val)
                trav(node.left, level+1)
                trav(node.right, level+1)
        trav(root, 0)
        return list(self.result.values())