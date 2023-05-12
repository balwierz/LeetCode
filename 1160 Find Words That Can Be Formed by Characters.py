class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cc = Counter(chars)
        return sum(len(w) for w in words if Counter(w) < cc)
