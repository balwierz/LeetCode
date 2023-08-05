class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        while prev.next:
            node = ListNode(gcd(prev.val, prev.next.val), prev.next)
            prev.next = node
            prev = node.next
        return head
