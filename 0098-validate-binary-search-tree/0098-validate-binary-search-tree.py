# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -inf
        self.res = True
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev >= node.val:
                    self.res = False
                self.prev = node.val
                inorder(node.right)
        inorder(root)
        return self.res

