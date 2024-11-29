# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lowest = None
        def trav(node):
            if not node:
                return False

            score = (node == p) + (node == q) + trav(node.left) + trav(node.right)
            if score > 1:
                self.lowest = node

            return score>0
        trav(root)
        return self.lowest