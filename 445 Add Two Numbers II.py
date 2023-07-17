# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = []
        r2 = []
        h = l1
        while h is not None:
            r1.append(h.val)
            h = h.next
        h = l2
        while h is not None:
            r2.append(h.val)
            h = h.next
        carry = 0
        ret = None
        while len(r1) or len(r2) or carry:
            val = carry
            if len(r1):
                val += r1.pop()
            if len(r2):
                val += r2.pop()
            carry, val = divmod(val, 10)
            #print(val)
            ret = ListNode(val, ret)
        return ret
