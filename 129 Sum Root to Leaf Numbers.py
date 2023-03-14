class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        ret = 0
        def dfs(node):
            nonlocal ret
            stack.append(str(node.val))
            if not node.left and not node.right:
                ret += int(''.join(stack))
            elif node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()
        dfs(root)
        return(ret)
