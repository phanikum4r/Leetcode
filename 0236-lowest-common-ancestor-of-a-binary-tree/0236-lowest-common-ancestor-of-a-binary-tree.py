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

            left = trav(node.left)
            right = trav(node.right)
            mid = (node == p) or (node == q)

            if mid + left + right >= 2:
                self.lowest = node

            return mid or left or right
        trav(root)
        return self.lowest