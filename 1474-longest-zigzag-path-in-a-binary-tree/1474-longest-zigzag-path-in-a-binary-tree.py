# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def trav(root,m,cur,direction):
            self.res=max(m,self.res)
            if root.left:
                if direction==1:
                    trav(root.left,max(cur+1,m),cur+1,0)
                else:
                    trav(root.left,max(cur,m),1,direction)
            if root.right:
                if direction==0:
                    trav(root.right,max(cur+1,m),cur+1,1)
                else:
                    trav(root.right,max(cur,m),1,direction)
        if root.left:
            trav(root.left,1,1,0)
        if root.right:
            trav(root.right,1,1,1)
        return self.res