# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([[root]])
        while q:
            cur = q.popleft()
            new = []
            result.append(cur[-1].val)
            for node in cur:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if new:
                q.append(new)
        return result