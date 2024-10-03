# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        slow = fast = head
        l = 1
        while fast.next is not None:
            fast = fast.next
            l += 1
        for _ in range(l - (k % l) - 1):
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
        