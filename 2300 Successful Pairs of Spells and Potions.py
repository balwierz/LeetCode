class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        for i, spell in enumerate(spells):
            target = ceil(success / spell)
            l = 0
            r = len(potions)-1
            if target <= potions[l]: 
                spells[i] = len(potions)
                continue
            if target > potions[r]:
                spells[i] = 0
                continue
            while l+1 < r:
                mid = (l+r) // 2
                if potions[mid] < target:
                    l = mid
                else:
                    r = mid
            print(target, l, r)
            spells[i] = len(potions) - r
        return spells
