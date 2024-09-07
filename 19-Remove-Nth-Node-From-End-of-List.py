# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = head
        for _ in range(n - 1):
            fast = fast.next
        while fast and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next
        if slow is head:
            if fast is slow:
                return None
            else:
                return head.next
        else:
            prev.next = slow.next if fast is not slow else None
            return head
        