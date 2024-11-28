# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur, last, prev = head, None, None
        seen = False
        while cur:
            if cur.val >= x:
                seen = True
                prev = cur
                cur = cur.next
            else:
                if not seen:
                    last = cur
                    prev = cur
                    cur = cur.next
                elif not last:
                    temp = cur.next
                    last = cur
                    last.next = head
                    head = last
                    cur = temp
                    prev.next = temp
                else:
                    prev.next = cur.next
                    cur.next = last.next
                    last.next = cur
                    last = cur
                    cur = prev.next
        return head   