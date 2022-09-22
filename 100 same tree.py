# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

def dfs(node0, node1):
    if node0.val != node1.val:
        return False
    if (node0.left is None) != (node1.left is None):
        return False
    if (node0.right is None) != (node1.right is None):
        return False
    if not (node0.left is None):
        if not dfs(node0.left, node1.left):
            return False
    if not (node0.right is None):
        if not dfs(node0.right, node1.right):
            return False
    return True
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) != (q is None):
            return False
        if p is None:
            return True
        return dfs(p, q)
