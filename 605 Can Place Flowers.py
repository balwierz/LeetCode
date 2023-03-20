    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = '$' + ''.join([str(plot) for plot in flowerbed]) + '$'
        return sum([(len(bed)-1)//2 for bed in p.split('1')]) >= n
