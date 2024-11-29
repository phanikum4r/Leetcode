"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([[root]])
        while q:
            child_list = []
            cur_list = q.popleft()
            for i in range(len(cur_list)-1):
                cur_list[i].next = cur_list[i+1]
                if cur_list[i].left:
                    child_list.append(cur_list[i].left)
                if cur_list[i].right:
                    child_list.append(cur_list[i].right)
            cur_list[-1].next = None
            if cur_list[-1].left:
                child_list.append(cur_list[-1].left)
            if cur_list[-1].right:
                child_list.append(cur_list[-1].right)
            if child_list:
                q.append(child_list)
        return root