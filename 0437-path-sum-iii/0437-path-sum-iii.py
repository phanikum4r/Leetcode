# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathsum=0
        self.res=0
        h=defaultdict(int)
        def trav(root,pathsum):
            if root:
                pathsum+=root.val    
                if pathsum==targetSum:
                    self.res+=1
                self.res+=h[pathsum-targetSum]
                h[pathsum]+=1
                trav(root.left,pathsum)
                trav(root.right,pathsum)
                h[pathsum]-=1
        trav(root,pathsum)
        return self.res