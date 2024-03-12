def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0, head)  # new head
    cumsum = 0
    sum2firstPos = {}
    it = head
    while it:
        cumsum += it.val
        it.cs = cumsum
        if cumsum in sum2firstPos:
            it2 = sum2firstPos[cumsum].next
            while it2 != it:
                del sum2firstPos[it2.cs]
                it2 = it2.next
            sum2firstPos[cumsum].next = it.next
        else:
            sum2firstPos[cumsum] = it
        it = it.next
    return head.next
