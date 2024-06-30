# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        m=-10001
        self.res=0
        def trav(root,m):
            if root:
                if root.val>=m:
                    self.res+=1
                    m=root.val
                trav(root.left,m)
                trav(root.right,m)
        trav(root,m)
        return self.res