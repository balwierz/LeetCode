# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        def helper(i, j):
            nonlocal arr
            if i > j:
                return None
            mid = (i+j) // 2
            return TreeNode(arr[mid], helper(i, mid-1), helper(mid+1, j))
        return helper(0, len(arr)-1)
