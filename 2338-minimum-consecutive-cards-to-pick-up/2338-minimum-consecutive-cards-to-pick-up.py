class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        freq = {}
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in freq:
                ans = min(ans, i - freq[cards[i]] + 1)
            freq[cards[i]] = i
        
        return ans if ans < float("inf") else -1