def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    q = deque()
    q.append(root)
    broken = False
    while q:
        q2 = deque()
        while(q):
            node = q.popleft()
            if node.left: q2.append(node.left)
            else:
                if node.right: return False
                broken = True
                break
            if node.right: q2.append(node.right)
            else:
                broken = True
                break
        if broken: break
        q = q2
    # now check if the remaining part of the row is empty:
    for q in [q, q2]:
        while q:
            node = q.popleft()
            if node.left or node.right: return False
    return True
