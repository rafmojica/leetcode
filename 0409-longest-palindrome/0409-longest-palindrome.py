class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        finalCount = 0
        hasOdd = False

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in freq.values():
            finalCount += (c // 2) * 2
            if c % 2:
                hasOdd = True
        
        if hasOdd:
            return finalCount + 1
        else:
            return finalCount