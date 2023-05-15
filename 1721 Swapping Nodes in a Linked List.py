# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(k - 1):
            fast = fast.next
        first = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        first.val, slow.val = slow.val, first.val
        return head

class Solution2:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = k
        j = k
        a = None
        b = None
        def helper(node):
            nonlocal i, j, a, b
            i -= 1
            if i == 0:
                a = node
            if node.next:
                helper(node.next)
            j -= 1
            if j == 0:
                b = node
        helper(head)
        a.val, b.val = b.val, a.val
        return(head)
        
