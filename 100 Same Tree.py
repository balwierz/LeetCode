class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []
            ret = [node.val]
            if node.left:
                ret.append("L")
                ret.append(dfs(node.left))
            if node.right:
                ret.append("R")
                ret.append(dfs(node.right))
            ret.append("P")
            return ret
        return dfs(p) == dfs(q)
