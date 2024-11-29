# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            root_val = postorder[postorder_index]
            root = TreeNode(root_val, None, None)
            postorder_index -= 1
            root.right = build(inorder_map[root_val]+1, right)
            root.left = build(left, inorder_map[root_val]-1)
            return root
        inorder_map = {}
        postorder_index = len(inorder) - 1
        for key, value in enumerate(inorder):
            inorder_map[value] = key
        return build(0, len(inorder) - 1)