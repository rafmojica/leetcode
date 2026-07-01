class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        maxVal = max(freq.values())

        return sum(v for v in freq.values() if v == maxVal)
        