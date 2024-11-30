# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = {}
        def trav(node, level):
            if node:
                if level%2==0:
                    self.result.setdefault(level, []).append(node.val)
                else:
                    self.result.setdefault(level, []).insert(0,node.val)
                trav(node.left, level+1)
                trav(node.right, level+1)
        trav(root, 0)
        return list(self.result.values())