from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        total = 0

        for num in nums:
            freq[num] += 1

        for num in freq:
            if freq[num] == 1:
                total += num

        return total
        