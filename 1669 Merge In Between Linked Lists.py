class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        b -= a - 1
        while a > 1:
            head = head.next
            a -= 1
        r = head.next
        head.next = list2
        while head.next:
            head = head.next
        while b:
            r = r.next
            b -= 1
        head.next = r
        return list1
        
