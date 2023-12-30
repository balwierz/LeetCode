def makeEqual(self, w: List[str]) -> bool:
    return not any(x%len(w) for x in Counter(''.join(w)).values())
