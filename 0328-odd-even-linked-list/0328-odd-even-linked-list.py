# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        first=head
        last=head.next
        while last.next:
            last=last.next
        flag=last
        while first!=flag and first.next.next:
            if first.next==flag:
                temp=first.next
                first.next=first.next.next
                temp.next=None
                last.next=temp
                last=last.next
                break
            temp=first.next
            first.next=first.next.next
            first=first.next
            temp.next=None
            last.next=temp
            last=last.next
        return head