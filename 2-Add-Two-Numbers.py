class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            leftover = sum % 10
            carry = sum // 10

            node = ListNode(leftover)
            cur.next = node
            cur = cur.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return head.next
            


