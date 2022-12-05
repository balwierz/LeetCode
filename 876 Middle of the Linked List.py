# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        slow, fast = head, head
        while True:
            slow = slow.next
            for _ in (0, 1):
                fast = fast.next
                if fast == None or fast.next == None:
                    return slow
