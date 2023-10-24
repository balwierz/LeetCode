def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    if not root: return []
    ret = []
    thisRow = [root]
    while thisRow:
        nextRow = [x.left for x in thisRow if x.left] + [x.right for x in thisRow if x.right]
        ret.append(max([x.val for x in thisRow]))
        thisRow = nextRow
    return ret
