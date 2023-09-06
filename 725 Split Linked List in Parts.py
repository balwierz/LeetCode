def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    l = 0
    p = head
    while p:
        l += 1
        p = p.next
    d, m = divmod(l, k)
    ret = []
    for _ in range(k):
        ret.append(head)
        n = d + (1 if m else 0)
        if n:
            for _ in range(n-1):
                head = head.next
            next = head.next
            head.next = None
            head = next
        if m:
            m -= 1
    return ret
