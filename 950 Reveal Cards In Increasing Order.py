def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    deck.sort(reverse=True)
    d = deque(range(len(deck)))
    ret = [0] * len(deck)
    while d:
        ret[d.popleft()] = deck.pop()
        if d:
            d.append(d.popleft())
    return ret
