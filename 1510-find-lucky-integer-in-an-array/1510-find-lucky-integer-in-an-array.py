class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        maxElem = -1
        for k, v in freq.items():
            if v == k:
                maxElem = max(maxElem, v)

        return maxElem