class Solution:
    def minMaxDifference(self, num: int) -> int:
        num1 = list(str(num))
        num2 = list(str(num))
        toReplace = ''
        for d in num1:
            if d != '9':
                toReplace = d
                break
        first = num2[0]
        for i in range(len(num1)):
            if num1[i] == toReplace:
                num1[i] = '9'
            if num2[i] == first:
                num2[i] = '0'
        
        return int(''.join(num1)) - int(''.join(num2))
