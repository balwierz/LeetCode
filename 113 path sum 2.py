# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
        self.ret = []
        self.sum = 0
    def setArgs(self, target):
        self.target = target
    def dfs(self, node):   # node is not None
        self.sum += node.val
        self.stack.append(node.val)
        if (not node.left) and (not node.right):  #leaf
            if self.sum == self.target:
                self.ret.append(self.stack.copy())
        else:
            if(node.left):
                self.dfs(node.left)
            if node.right:
                self.dfs(node.right)
        self.sum -= node.val
        self.stack.pop()
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.setArgs(targetSum)
        if root is None:
            return []
        self.dfs(root)
        return self.ret
