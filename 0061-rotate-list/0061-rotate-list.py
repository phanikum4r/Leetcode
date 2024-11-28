# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        cur, n = head, 0
        while cur:
            n += 1
            last = cur
            cur = cur.next
        k = k % n
        n -= k
        if n == 0:
            return head
        cur = head
        while n>1:
            cur = cur.next
            n -= 1
        last.next = head
        head = cur.next
        cur.next = None
        return head