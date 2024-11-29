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
        # using queue    
        # q = deque([[root]])
        # while q:
        #     child_list = []
        #     cur_list = q.popleft()
        #     for i in range(len(cur_list)):
        #         if i < len(cur_list) - 1:
        #             cur_list[i].next = cur_list[i+1]
        #         if cur_list[i].left:
        #             child_list.append(cur_list[i].left)
        #         if cur_list[i].right:
        #             child_list.append(cur_list[i].right)
        #     if child_list:
        #         q.append(child_list)
        # return root

        # using pointers with constant space, leftmost for next level start, prev for linking
        leftmost, prev = root, None
        cur = root
        while leftmost:
            cur = leftmost
            prev, leftmost = None, None
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        leftmost = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        leftmost = cur.right
                    prev = cur.right
                cur = cur.next
        return root