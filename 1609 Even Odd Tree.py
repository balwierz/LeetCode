# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        lvl = 0
        while q:
            n = len(q)
            lq = list(q)
            if lvl == 0:
                if any(a.val >= b.val for a, b in pairwise(lq)) or any(x.val % 2 == 0 for x in lq):
                    return False
            else:
                if any(a.val <= b.val for a, b in pairwise(lq)) or any(x.val % 2 == 1 for x in lq):
                    return False
            while n:
                n -= 1
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl = 1 - lvl
        return True


        
