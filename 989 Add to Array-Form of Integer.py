class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k = [int(d) for d in str(k)]
        carry = 0
        ret = []
        m = max(len(num), len(k))
        num = list(reversed(num))
        k = list(reversed(k))
        for i in range(m):
            a = num[i] if i < len(num) else 0
            b = k[i]   if i < len(k)   else 0
            carry, d = divmod(a + b + carry, 10)
            ret.append(d)
        if carry: ret.append(carry)
        return list(reversed(ret))
