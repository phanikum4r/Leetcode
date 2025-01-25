# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        tree = []
        def inorder(node):
            if node:
                inorder(node.left)
                tree.append(node.val)
                inorder(node.right)
        inorder(root)
        left, right = 0, len(tree)-1
        while left < right:
            if tree[left] + tree[right] == k:
                return True
            elif tree[left] + tree[right] > k:
                right -= 1
            else:
                left += 1
        return False