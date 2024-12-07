# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(head1, head2):
            head = node = ListNode(0)
            while head1 and head2:
                if head1.val <= head2.val:
                    node.next = head1
                    head1 = head1.next
                else:
                    node.next = head2
                    head2 = head2.next
                node = node.next
            if head1:
                node.next = head1
            if head2:
                node.next = head2
            return head.next

        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval*2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if n else None