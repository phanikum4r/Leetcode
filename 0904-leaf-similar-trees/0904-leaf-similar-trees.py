# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1,l2=[],[]
        def trav(root,l):
            if root:
                if not root.left and not root.right:
                    l.append(root.val)
                else:
                    trav(root.left,l)
                    trav(root.right,l)
        trav(root1,l1)
        trav(root2,l2)
        if len(l1)==len(l2):
            for i in range(len(l1)):
                if l1[i]!=l2[i]:
                    return False
            return True
        else:
            return False