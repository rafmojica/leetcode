class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # create hashmap counting the num of characters.
        # 1 b, 1 a, 2 l, 2 o, 1 n
        freq = {}
        for c in text:
            freq[c] = freq.get(c, 0) + 1
            
        return min(freq.get('b', 0), freq.get('a', 0), freq.get('l', 0) // 2, freq.get('o', 0) // 2, freq.get('n', 0))
        