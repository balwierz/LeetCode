def countSubstrings(self, s: str, c: str) -> int:
    return (n := s.count(c))*(n+1) // 2
