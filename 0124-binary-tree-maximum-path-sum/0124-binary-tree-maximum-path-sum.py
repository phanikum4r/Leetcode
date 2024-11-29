# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        def pathsum(node):
            if not node:
                return 0
            left = max(pathsum(node.left), 0)
            right = max(pathsum(node.right), 0)
            self.maxSum = max(self.maxSum, node.val + left + right)
            return node.val + max(left, right)
        pathsum(root)
        return self.maxSum