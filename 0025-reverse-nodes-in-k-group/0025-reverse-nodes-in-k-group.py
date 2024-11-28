# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==1:
            return head
        cur, prev = head, None
        i, j, n = 1, 1, 0
        while cur:
            n += 1
            cur = cur.next
        n = (n//k) * k
        cur = head
        while cur:
            if i == 1:
                last = cur
                prev_group_last = prev
                prev = cur
                cur = cur.next
            elif i<k:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            else:
                last.next = cur.next
                cur.next = prev
                prev = last
                if head == last:
                    head = cur
                else:
                    prev_group_last.next = cur
                cur = last.next
            i = 1 if i == k else i+1
            j += 1
            if j>n:
                break
        return head