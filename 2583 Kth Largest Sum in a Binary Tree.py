class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        def dfs(node, lvl):
            if not node: return
            nonlocal sums
            if len(sums)-1 < lvl:
                sums.append(node.val)
            else:
                sums[lvl] += node.val
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)
        dfs(root, 0)
        if len(sums) < k: return -1
        sums.sort(reverse = True)
        return sums[k-1]
