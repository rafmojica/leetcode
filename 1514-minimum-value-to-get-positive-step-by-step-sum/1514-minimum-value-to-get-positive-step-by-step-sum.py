class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = min_val = 0

        for num in nums:
            total += num
            min_val = min(min_val, total)

        return 1 - min_val
        