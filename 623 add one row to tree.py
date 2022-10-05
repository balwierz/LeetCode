# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        lvl = 1
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            root = node
            return root
        while lvl < depth-1:
            w = len(q)
            for _ in range(w):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        while len(q):
            node = q.popleft()
            nodeL = TreeNode(val)
            nodeL.left = node.left
            node.left = nodeL
            nodeR = TreeNode(val)
            nodeR.right = node.right
            node.right = nodeR
        return root
