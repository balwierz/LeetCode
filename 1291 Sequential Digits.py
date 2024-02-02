def sequentialDigits(self, low: int, high: int) -> List[int]:
    return [int(''.join([str(x) for x in range(i,i+L)])) for L in range(len(str(low)), 1+len(str(high))) for i in range(1, 11-L) if low <= int(''.join([str(x) for x in range(i,i+L)])) <= high]        
