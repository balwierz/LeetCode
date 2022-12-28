class Solution:
    def smallestValue(self, n: int) -> int:
        if n == 4: return 4
        tab = [0, n]
        while len(tab) > 1:
            n = sum(tab)
            newtab = []
            i = 2
            while i <= int(sqrt(n)):
                if n % i == 0:
                    n /= i
                    newtab.append(i)
                else:
                    i += 1
            tab = newtab
            tab.append(n)
        return int(tab[0])
