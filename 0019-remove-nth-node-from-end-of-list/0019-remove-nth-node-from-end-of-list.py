# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        first, second = head, head
        for i in range(n):
            first = first.next
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head


        # 2 pass
        # cur = head
        # count = 0
        # while cur:
        #     count+=1
        #     cur = cur.next
        # count -= n
        # if not count:
        #     return head.next
        # cur = head
        # while count>1:
        #     cur = cur.next
        #     count -= 1
        # cur.next = cur.next.next
        # return head