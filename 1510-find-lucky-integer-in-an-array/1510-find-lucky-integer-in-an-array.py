class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        return max([v if v == k else -1 for k, v in freq.items()])