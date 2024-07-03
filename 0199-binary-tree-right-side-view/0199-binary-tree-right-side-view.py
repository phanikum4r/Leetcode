# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res={}
        def trav(root,level):
            if root:
                self.res[level]=root.val
                trav(root.left,level+1)
                trav(root.right,level+1)
        trav(root,0)
        return self.res.values()