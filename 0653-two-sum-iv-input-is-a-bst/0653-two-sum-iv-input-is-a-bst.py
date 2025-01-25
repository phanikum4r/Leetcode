# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        tree = set()
        def inorder(node):
            if node:
                if k - node.val in tree:
                    return True
                tree.add(node.val)
                return inorder(node.left) or inorder(node.right)
            return False
        return inorder(root)