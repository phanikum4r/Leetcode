# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        n=0
        temp=head
        while(temp):
            temp=temp.next
            n+=1
        n=n//2
        temp=head
        while n>1:
            temp=temp.next
            n-=1
        temp.next=temp.next.next
        return head