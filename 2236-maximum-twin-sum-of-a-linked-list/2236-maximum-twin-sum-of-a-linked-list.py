# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=0
        slow=fast=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        while slow:
            res=max(res,(slow.val+prev.val))
            slow=slow.next
            prev=prev.next
        return res