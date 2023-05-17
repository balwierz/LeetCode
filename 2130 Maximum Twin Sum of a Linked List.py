class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ret = 0
        def helper(node):
            nonlocal ret, head
            if node.next:
                helper(node.next)
            ret = max(ret, head.val + node.val)
            head = head.next
        helper(head)
        return ret
