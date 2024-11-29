# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def pathsum(node, cur):
            if not node.left and not node.right:
                self.result += int(cur + str(node.val))
            if node.left:
                pathsum(node.left, cur + str(node.val))
            if node.right:
                pathsum(node.right, cur + str(node.val))
        pathsum(root, "")
        return self.result