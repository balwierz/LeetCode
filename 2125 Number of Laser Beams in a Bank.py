class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return sum(map(prod, pairwise(filter(bool, (x.count("1") for x in bank)))))
