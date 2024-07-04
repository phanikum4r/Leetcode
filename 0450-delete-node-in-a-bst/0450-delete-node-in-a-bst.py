# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(root):
            root=root.right
            while root.left:
                root=root.left
            return root.val
        def predecessor(root):
            root=root.left
            while root.right:
                root=root.right
            return root.val
        def delete(root,key):
            if root:
                print(root.val)
                if key>root.val:
                    root.right=delete(root.right,key)
                elif key<root.val:
                    root.left=delete(root.left,key)
                else:
                    if not (root.left or root.right):
                        return None
                    elif root.right:
                        root.val=successor(root)
                        root.right=delete(root.right,root.val)
                    elif root.left:
                        root.val=predecessor(root)
                        root.left=delete(root.left,root.val)
                return root
            else:
                return None
        return delete(root,key)