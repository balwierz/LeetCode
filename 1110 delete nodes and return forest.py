# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = set()
        preRoot = TreeNode(left=root)
        to_delete = set(to_delete)
        def dfs(node, parent, link):
            if node.left:
                dfs(node.left, node, 0)
            if node.right:
                dfs(node.right, node, 1)
   
            if node.val in to_delete:
                if(node.left): 
                    roots.add(node.left)
                if node.right: 
                    roots.add(node.right)
                if link==0:
                    parent.left = None
                elif link==1:
                    parent.right = None
        dfs(root, preRoot, 0)
        if not root.val in to_delete:
            roots.add(root)
        return list(roots)
