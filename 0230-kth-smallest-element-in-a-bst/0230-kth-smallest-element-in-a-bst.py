# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.idx = 0
        def inorder(node):
            if node:
                left = inorder(node.left)
                self.idx += 1
                if self.idx == k:
                    return node.val 
                else:
                    mid = 0     
                right = inorder(node.right)
                return left + right
            return 0
        return inorder(root)