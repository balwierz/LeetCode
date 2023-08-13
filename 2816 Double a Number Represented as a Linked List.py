class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        h = None
        def helper(node):
            nonlocal carry
            nonlocal h
            if not node:
                return
            helper(node.next)
            s = (node.val << 1) + carry
            carry = int(s>=10)
            h = ListNode(s%10, h)
        helper(head)
        if carry:
            h = ListNode(1, h)
        return h
