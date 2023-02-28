class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        h2done = {}
        ret = []
        def helper(node):
            nonlocal h2done
            if not node:
                return 28747753
            hl = helper(node.left)
            hr = helper(node.right)
            h = hash((hl, hr, node.val+9999999,))
            if h in h2done and h2done[h]:
                ret.append(node)
                h2done[h] = 0
            elif h not in h2done:
                h2done[h] = 1
            return h
        helper(root)
        return ret
