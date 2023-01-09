class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def pre(node):
            ret.append(node.val)
            if node.left:
                pre(node.left)
            if node.right:
                pre(node.right)
        if root: pre(root)
        return ret
