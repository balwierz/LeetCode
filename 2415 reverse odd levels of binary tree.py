# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelV = deque()
        q = deque()
        q.append(root)
        level = 0
        while len(q):
            # new level starts
            if level %2 == 0:
                for i in range(2**level):
                    node = q.popleft()
                    if(node.left):
                        q.append(node.left)
                        levelV.append(node.left.val)
                        q.append(node.right)
                        levelV.append(node.right.val)
            else: # odd level; restore values in reverse order
                for i in range(2**level):
                    node = q.popleft()
                    node.val = levelV.pop()
                    if(node.left):
                        q.append(node.left)
                        q.append(node.right)
            level += 1
        return root
