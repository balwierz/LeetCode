# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #ret = root.val

        def helper(node, fromTopRight):  # returns total of the subtree
            ret = node.val
            node.val += fromTopRight
            if node.right:
                x = helper(node.right, fromTopRight)
                node.val += x
                ret += x
            if node.left:
                x = helper(node.left, node.val)
                ret += x
            return ret

        helper(root, 0)
        return root
