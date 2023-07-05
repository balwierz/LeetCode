class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve(n):
            isPrime = [True] * n
            for x in range(2, int(sqrt(n))+1):
                if isPrime[x]:
                    for y in range(x*2, n, x):
                        isPrime[y] = False
            return isPrime
        isPrime = sieve(n)
        ret = []
        for x in range(2, n//2+1):
            if isPrime[x] and isPrime[n-x]:
                ret.append((x, n-x))
        return ret
