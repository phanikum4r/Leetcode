# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def build(node):
            if not node:
                return node, node
                
            leftHead, leftTail = build(node.left)
            rightHead, rightTail = build(node.right)

            if leftHead:
                leftTail.right = node
                node.left = None
            else:
                leftHead = node

            if rightHead:
                node.right = rightHead
            else:
                rightTail = node

            return [leftHead, rightTail]
        self.root = TreeNode(-inf, None, build(root)[0])

    def next(self) -> int:
        if self.root and self.root.right:
            self.root = self.root.right
            return self.root.val
        else:
            return 0

    def hasNext(self) -> bool:
        return True if self.root.right else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()