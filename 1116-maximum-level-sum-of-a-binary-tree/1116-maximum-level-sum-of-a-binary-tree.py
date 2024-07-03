# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res=[float('-inf'),-1]
        c=0
        q=deque()
        q.append(root)
        while q:
            c+=1
            n=len(q)
            cur=None
            cur_sum=0
            next_level=[]
            for i in range(n):
                cur=q.popleft()
                cur_sum+=cur.val
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            if cur_sum>res[0]:
                res[0]=cur_sum
                res[1]=c
            for i in next_level:
                q.append(i)
        return res[1]