# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            root = TreeNode(root_val, None, None)
            preorder_index += 1
            root.left = build(left, inorder_map[root_val]-1)
            root.right = build(inorder_map[root.val]+1, right)
            return root
        inorder_map = {}
        preorder_index = 0
        for key, value in enumerate(inorder):
            inorder_map[value] = key
        return build(0, len(inorder)-1)