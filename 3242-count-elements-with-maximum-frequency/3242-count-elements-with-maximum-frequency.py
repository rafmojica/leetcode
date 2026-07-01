class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = 0
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        maxVal = max(freq.values())

        for k, v in freq.items():
            if v == maxVal:
                maxFreq += maxVal

        return maxFreq
        