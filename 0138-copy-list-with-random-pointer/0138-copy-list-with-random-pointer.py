"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        oldHead = head
        original = {oldHead:0}
        newHead = Node(oldHead.val,oldHead.next,oldHead.random)
        dup = {0:newHead}
        temp = newHead
        oldHead = oldHead.next
        i = 1
        while oldHead:
            original[oldHead] = i
            new = Node(oldHead.val,oldHead.next,oldHead.random)
            dup[i]=new
            temp.next = new
            temp = temp.next
            oldHead = oldHead.next
            i += 1
        temp = newHead
        oldHead = head
        while temp:
            temp.random = dup[original[oldHead.random]] if oldHead.random else None
            temp = temp.next
            oldHead = oldHead.next
        return newHead