# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev, flag = None, 0
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
                flag = 1
            if flag:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
                flag = 0
            else:
                prev = cur
            cur = cur.next
        return head