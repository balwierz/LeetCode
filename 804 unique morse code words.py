code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
        "...","-","..-","...-",".--","-..-","-.--","--.."]
toMorse = lambda x: "".join(map(lambda c: code[ord(c)-ord('a')], x))
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(map(toMorse, words)))
