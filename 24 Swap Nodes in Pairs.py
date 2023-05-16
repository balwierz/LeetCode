class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next): return head 
        node=head.next 
        head.next=self.swapPairs(head.next.next) 
        node.next=head 
        return node 

class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(val=-1, next=head)  # true head
        prev = h
        while True:
            if not prev.next or not prev.next.next:
                break
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            b.next = a
            a.next = c
            prev = a
        return h.next
