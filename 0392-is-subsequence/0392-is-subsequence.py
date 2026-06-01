class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # using two pointers
        # O(n) time, O(1) space
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]: # move both
                i += 1
                j += 1
            else: # move j
                j += 1

        return i == len(s)
