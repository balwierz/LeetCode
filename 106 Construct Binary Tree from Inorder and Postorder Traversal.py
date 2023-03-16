def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    node = TreeNode(postorder[-1])
    i = 0
    while inorder[i] !=  postorder[-1]: i += 1
    if i:
        node.left = self.buildTree(inorder[0:i], postorder[0:i])
    if len(inorder) - i - 1:
        node.right = self.buildTree(inorder[(i+1):len(postorder)], postorder[(i):(len(postorder)-1)])
    return node
