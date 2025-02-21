class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        if target == 0:
            return True
        target += 1
        mask = 1 << (target.bit_length() - 2)
        p = self.root
        while mask:
            p = p.right if target & mask else p.left
            if p is None:
                return False
            mask >>= 1
        return True
