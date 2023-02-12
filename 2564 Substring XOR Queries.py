class Node:
    def __init__(self):
        self.leafOf = []
        self.left, self.right = None, None

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        toFind = [format(first ^ second, 'b') for first, second in queries]
        root = Node()
        for i, vir in enumerate(toFind):
            cur = root
            for c in vir:
                if c == '0':
                    if cur.left == None:
                        cur.left = Node()
                    cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = Node()
                    cur = cur.right
            cur.leafOf.append(i)
        ret = [[-1, -1] for _ in range(len(toFind))]
        iterators = []
        for i, c in enumerate(s):
            newIterators = []
            iterators.append((i, root))
            for start, pos in iterators:
                if c == '0' and pos.left:
                    pos = pos.left
                elif c == '1' and pos.right:
                    pos = pos.right
                else:
                    continue
                newIterators.append((start, pos))
                for leaf in pos.leafOf:
                    if ret[leaf][0] == -1:
                        ret[leaf] = [start, i]
            iterators = newIterators
        return ret
