# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def depth(head, n):
    # returns the depth and removes the element if necessary
    if head.next == None:
        return 1
    level = depth(head.next, n) + 1
    if level == n+1:
        # remove the element
        if n==1:
            head.next = None
        else:
            head.next = head.next.next
    return level

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prehead = ListNode(0, head)
        depth(prehead, n)
        return prehead.next
