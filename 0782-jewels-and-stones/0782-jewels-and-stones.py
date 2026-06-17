from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = defaultdict(int)
        ans = 0
        
        for stone in stones:
            freq[stone] += 1
        
        for jewel in jewels:
            if jewel in freq:
                ans += freq.get(jewel)
                
        return ans
        