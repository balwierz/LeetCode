def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None
    slow = head.next
    fast = head.next.next
    while slow != fast:
        slow = slow.next
        if not fast or not fast.next:
            return None
        fast = fast.next.next
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
