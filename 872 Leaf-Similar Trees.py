class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        buf = [[],[]]
        def tree2leafs(root):
            nonlocal buf
            nonlocal bufI
            if root.left == None and root.right == None:
                buf[bufI].append(root.val)
            if root.left:
                tree2leafs(root.left)
            if root.right:
                tree2leafs(root.right)
        bufI = 0
        tree2leafs(root1)
        bufI = 1
        tree2leafs(root2)
        return buf[1] == buf[0]
