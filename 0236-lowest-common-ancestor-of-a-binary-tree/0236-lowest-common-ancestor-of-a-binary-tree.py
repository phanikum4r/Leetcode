# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res=root
        def trav(root,p,q):
            if root:
                a=(trav(root.left,p,q)+trav(root.right,p,q)+(root==p)+(root==q))
                if a>1:
                    self.res=root
                    return 0
                else:
                    return a
            else:
                return 0
        trav(root,p,q)
        return self.res
        