def firstPalindrome(self, words: List[str]) -> str:
    return next((w for w in words if w[:len(w)//2] == w[:-(len(w)//2)-1:-1]), "")
