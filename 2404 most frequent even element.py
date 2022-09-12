class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter([num for num in nums if num % 2 == 0])
        if(not c):
            return -1
        k = c.most_common(1)[0];
        #print(k)
        a = [num for num in c.keys() if c[num] == c[k[0]]]
        return(min(a))
        
