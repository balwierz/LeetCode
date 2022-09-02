# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = deque([root])
        ret = []
        while len(d):
            li = len(d)
            s = 0
            for i in range(li):
                p = d.popleft()
                s += p.val
                if p.left:
                    d.append(p.left)
                if p.right:
                    d.append(p.right)
            ret.append(s/li)
        return ret
