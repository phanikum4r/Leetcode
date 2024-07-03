# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def trav(root):
            if not root or root.val==val:
                return root
            if root.val>val:
                return trav(root.left)
            else:
                return trav(root.right)
        return trav(root)