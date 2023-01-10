# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def parseDigits(txt, i):
            ret = []
            while i<len(txt) and txt[i].isdigit():
                ret.append(txt[i])
                i += 1
            return(int(''.join(ret)), i)
        def parseMinus(txt, i):
            ret = 0
            while i<len(txt) and txt[i] == '-':
                i += 1
                ret += 1
            return (ret, i)
        
        ladder = []
        if not traversal: return None
        lastDepth = 0
        i = 0
        rootVal, i = parseDigits(traversal, i)
        ladder.append(TreeNode(rootVal))
        while i<len(traversal):
            depth, i = parseMinus(traversal, i)
            val, i =   parseDigits(traversal, i)
            # print("d", depth, " v",  val)
            if depth > lastDepth:
                if len(ladder)-1 < depth:
                    ladder.append(TreeNode(val))
                else:
                    ladder[depth] = TreeNode(val)
                ladder[depth-1].left = ladder[depth]
                #print(ladder[depth-1].val, " leftpoints to ", ladder[depth].val)
            else:
                ladder[depth] = TreeNode(val)
                ladder[depth-1].right = ladder[depth]
            lastDepth = depth
        return ladder[0]

