# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np

class Solution:
  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    # We will use a stack to keep track of the nodes we have created so far
    stack = []
    for num in nums:
        node = TreeNode(num)       
        # If the stack is not empty and the current number is greater than the top of the stack,
        # we need to pop the stack until we find a node with a value greater than the current number.
        # The last popped node will be the parent of the current node.
        while stack and num > stack[-1].val:
            node.left = stack.pop()
        
        # If the stack is not empty, the top node is the parent of the current node.
        # We set the right child of the parent to be the current node.
        if stack:
            stack[-1].right = node
        
        # We push the current node onto the stack.
        stack.append(node)
    
    # The last node on the stack is the root of the tree.
    return stack[0]

class Solution2:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nums = np.array(nums)
        def build(arr):
            if not len(arr):
                return None
            ind = np.argmax(arr)
            return TreeNode(arr[ind], build(arr[:ind]), build(arr[ind+1:]))
            
        return build(nums)
