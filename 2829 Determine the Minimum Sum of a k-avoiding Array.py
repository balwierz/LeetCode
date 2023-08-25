class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # 1, 2: 3   # 3: max 1
        # 1, 2, 3: 3, 4, 5   # 4: max 2, 5: max 2
        # 1, 2, 3, 4: 3, 4, 5, 6, 7  # 6: max 3, 7: max 3 
        mm = k // 2
        if n <= mm:
            return n * (n+1) // 2
        ret = mm * (mm+1) // 2
        # k -- k-1+n-mm
        ret += (k+k-1+n-mm) * (n-mm) // 2
        return ret
