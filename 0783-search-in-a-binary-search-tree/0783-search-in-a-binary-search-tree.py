# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def trav(root):
            if root:
                if root.val==val:
                    return root
                left=trav(root.left)
                right=trav(root.right)
                if left:
                    return left
                if right:
                    return right
            return None
        return trav(root)