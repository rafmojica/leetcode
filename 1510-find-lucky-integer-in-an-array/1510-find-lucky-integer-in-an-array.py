class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # constraints are 1-500. no need for hashmap (due to overhead)
        freq = [0] * 501

        for num in arr:
            freq[num] += 1

        maxElem = -1
        for num in arr:
            if freq[num] == num:
                maxElem = max(maxElem, freq[num])

        return maxElem