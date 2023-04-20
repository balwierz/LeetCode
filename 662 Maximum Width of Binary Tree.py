class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        ret = 0
        while q:
            nextQ = []
            ret = max(ret, q[-1][1] - q[0][1])
            for node, pos in q:
                if node.left: nextQ.append((node.left, pos*2))
                if node.right:nextQ.append((node.right, pos*2+1))
            q = nextQ
        return ret + 1
