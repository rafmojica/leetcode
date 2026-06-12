class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # create hashmap counting the num of characters.
        # 1 b, 1 a, 2 l, 2 o, 1 n
        freq = {}
        bCount, aCount, lCount, oCount, nCount, finalCount = 0, 0, 0, 0, 0, 0
        for c in text:
            freq[c] = freq.get(c, 0) + 1
            
        for letter in freq:
            if letter == 'b':
                bCount = freq.get(letter)
            if letter == 'a':
                aCount = freq.get(letter)
            if letter == 'l':
                lCount = freq.get(letter)
            if letter == 'o':
                oCount = freq.get(letter)
            if letter == 'n':
                nCount = freq.get(letter)
                
        while bCount >= 1 and aCount >= 1 and lCount >= 2 and oCount >= 2 and nCount >= 1:
            bCount -= 1
            aCount -= 1
            lCount -= 2
            oCount -= 2
            nCount -= 1
            finalCount += 1
            
        return finalCount
        