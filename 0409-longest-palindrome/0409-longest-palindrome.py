class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 1. store the frequency of each character in a hashmap
        # 2. declare a count variable
        # 3. loop through every char in hashmap, adding it's value to count if even, or odd (once only)
        # abababa
        # ccc
        # cabbacc --> cabcbac
        # abbccddd --> cbdadbc
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        isOdd = False
        count = 0
        for c in freq:
            if freq[c] % 2 == 0:
                count += freq[c]
            else:
                count += freq[c] - 1
                isOdd = True

        return count + 1 if isOdd else count