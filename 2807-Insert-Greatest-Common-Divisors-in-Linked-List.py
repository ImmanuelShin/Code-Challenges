# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        cur = head.next
        prev = head

        while cur:
            node = ListNode(math.gcd(prev.val, cur.val), cur)
            prev.next = node
            prev = cur
            cur = cur.next
        return head

            