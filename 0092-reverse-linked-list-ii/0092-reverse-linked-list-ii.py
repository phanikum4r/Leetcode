# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left >= right:
            return head
        i = 1
        temp = head
        start = None
        while i<left:
            start = temp
            temp = temp.next
            i += 1
        last = temp
        prev = None
        while i<=right:
            cur = temp.next
            temp.next = prev
            prev = temp
            temp = cur
            i += 1
        last.next = temp
        if start:
            start.next = prev
        else:
            head = prev
        return head