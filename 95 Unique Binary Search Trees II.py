# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(nums):
            return [TreeNode(nums[i], l, r) for i in range(len(nums)) for l in dfs(nums[:i]) for r in dfs(nums[i+1:])] if nums else [None]
        return dfs(range(1, n+1))

class Solution2:
    def init(self, m):
        self.trees = [[] for _ in range(9)]
        self.trees[0] = [None]
        self.trees[1].append(TreeNode(1))
        def addValueToTree(tree, val):
            if not tree:
                return
            tree.val += val
            addValueToTree(tree.left, val)
            addValueToTree(tree.right, val)

        for n in range(2, m+1):
            for lSize in range(n):
                rSize = n - lSize - 1
                for rTree in self.trees[rSize]:
                    rTree = copy.deepcopy(rTree)
                    addValueToTree(rTree, lSize+1)
                    for lTree in self.trees[lSize]:
                        self.trees[n].append(TreeNode(lSize+1, lTree, rTree))
                    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.init(n)
        return self.trees[n]
