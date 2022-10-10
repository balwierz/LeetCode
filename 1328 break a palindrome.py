class Solution:
    def breakPalindrome(self, pal: str) -> str:
        pal = [x for x in pal]
        if len(pal) <= 1:
            return ""
        for i in range(len(pal)//2):
            if(pal[i] != 'a'):
                pal[i] = 'a';
                return ''.join(pal)
        # we checked that the first half is a string of "aaaaa"
        pal[len(pal)-1] = 'b'
        return ''.join(pal)
