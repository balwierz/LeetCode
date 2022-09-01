# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([[root, root.val]])
        ret = 1
        while len(q):
            par, maxVal = q.popleft()
            for e in (par.left, par.right):
                if e:
                    q.append((e, max(maxVal, e.val)))
                    if e.val >= maxVal:
                        ret += 1
        return ret
