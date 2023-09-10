def countOrders(self, n: int) -> int:
    ret = 1
    for i in range(n):
        ret *= (2*i+1)*(2*i+2) // 2
        ret %= 1000_000_007
    return ret
