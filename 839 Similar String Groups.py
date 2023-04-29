class ListNode:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.next = None
    def __str__(self):
        return str(self.a)+":"+str(self.b)+ (", " + str(self.next) if self.next else "")
    

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        n = len(strs)
        p = len(strs[0])

        dist = [[0] * n for _ in range(n)]
        head = ListNode(-1, -1)
        ptr = head
        for i in range(n-1):
            for j in range(i+1, n):
                ptr.next = ListNode(i, j)
                ptr = ptr.next
        
        #print(strs)
        #print(head)
        for i in range(p):
            ptr = head
            while ptr.next:
                if strs[ptr.next.a][i] != strs[ptr.next.b][i]:
                    dist[ptr.next.a][ptr.next.b] += 1
                    if dist[ptr.next.a][ptr.next.b] > 2:
                        ptr.next = ptr.next.next  # delete element
                    else:
                        ptr = ptr.next
                else:
                    ptr = ptr.next
                
        #print(head)

        # union find
        parent = [i for i in range(n)]
        ret = n
        def root(x):
            while parent[x] != x:
                x, parent[x] = parent[x], parent[parent[x]]
            return x

        def union(a, b):
            a, b = root(a), root(b)
            if a != b:
                parent[a] = b
                nonlocal ret
                ret -= 1
        
        ptr = head.next
        while ptr:
            union(ptr.a, ptr.b)
            ptr = ptr.next
        return ret
            
