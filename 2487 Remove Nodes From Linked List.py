# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node.next:
                return [node.val, node]
            maxVal, ref = helper(node.next)
            if node.val >= maxVal:
                node.next = ref
                return [node.val, node]
            else:
                return [maxVal, ref]
        return(helper(head)[1])
