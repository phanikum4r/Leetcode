# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        h1, h2 = l1, l2
        while h1 and h2:
            s = h1.val + h2.val + carry
            if s>9:
                h1.val = s-10
                carry = 1
            else:
                h1.val = s
                carry = 0
            h2.val = h1.val
            p1, p2 = h1, h2
            h1 = h1.next
            h2 = h2.next

        if h2:
            p1.next = h2
            h1 = h2

        while h1:
            s = h1.val + carry
            if s>9:
                h1.val = s-10
                carry = 1
            else:
                h1.val = s
                carry = 0
            p1 = h1
            h1 = h1.next

        if carry:
            p1.next=ListNode(carry)
        return l1