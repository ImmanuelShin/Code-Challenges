# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        cur = head
        while cur:
            d[cur] = cur.val
            cur = cur.next
        start = prev = None
        for key in sorted(d, key=d.get):
            key.next = None
            if prev is None:
                start = prev = key
            else:
                prev.next = key
                prev = key
        return start
                