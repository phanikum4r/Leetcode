# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum=root.val
        def trav(root):
            if root:
                left=max(0,trav(root.left))
                right=max(0,trav(root.right))
                cur_sum=root.val+left+right
                self.max_sum=max(self.max_sum,cur_sum)
                return root.val+max(left,right)
            else:
                return 0
        trav(root)
        return self.max_sum