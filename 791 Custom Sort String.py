def customSortString(self, order: str, s: str) -> str:
    c = Counter(s)
    return ''.join(x * c[x] for x in list(order) + list(set(c.keys()) - set(order)))
