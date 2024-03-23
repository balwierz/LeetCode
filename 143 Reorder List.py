class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fwd = head
        stop = False
        def helper(node):
            nonlocal fwd, stop
            if node.next:
                helper(node.next)
            if stop:
                return
            if node == fwd or node == fwd.next:
                node.next = None
                stop = True
                return
            ffwd = fwd.next
            fwd.next = node
            node.next = ffwd
            fwd = ffwd
        helper(head)
