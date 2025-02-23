class Solution:
    def constructFromPrePost(self, x: List[int], y: List[int]) -> Optional[TreeNode]:
        ix = x.index(y[-2]) if len(y) > 1 else 1
        return TreeNode(x[0], self.constructFromPrePost(x[1:ix], y[:ix-1]), self.constructFromPrePost(x[ix:] , y[ix-1:-1])) if x else None
