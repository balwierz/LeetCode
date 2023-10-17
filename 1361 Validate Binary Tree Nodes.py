def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    c = Counter(leftChild) + Counter(rightChild)
    seen = False
    for i in range(n):
        if c[i] == 0:
            if seen:
                return False
            else:
                seen = True
                root = i
        elif c[i] != 1:
            return False
    if not seen:
        return False
    seen = [False] * n
    def dfs(x):
        if x == -1:
            return
        seen[x] = True
        dfs(leftChild[x])
        dfs(rightChild[x])
    dfs(root)
    return all(seen)      
