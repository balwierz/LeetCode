# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        lvl = [root]
        while lvl:
            total = 0
            for par in lvl:
                if par.left: total += par.left.val
                if par.right: total += par.right.val
            nextLvl = []
            for par in lvl:
                a = total
                if par.left:  a -= par.left.val
                if par.right: a -= par.right.val
                if par.left:
                    par.left.val = a
                    nextLvl.append(par.left)
                if par.right:
                    par.right.val = a
                    nextLvl.append(par.right)
            lvl = nextLvl
        return root
