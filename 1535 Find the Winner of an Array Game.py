class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        if k == 1:
            return max(arr[0], arr[1])
        
        q = deque(arr[1:])
        A = arr[0]
        cnt = 0
        while True:
            B = q.popleft()
            if A > B:
                cnt += 1
                if cnt == k:
                    return A
                q.append(B)
            else:
                q.append(A)
                A = B
                cnt = 1
