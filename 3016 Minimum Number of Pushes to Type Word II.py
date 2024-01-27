def minimumPushes(self, word: str) -> int:
    return sum(x * (i//8+1) for i, x in enumerate(sorted(Counter(word).values())[::-1]))
