from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = 0
        ans = -1
        count = defaultdict(int)

        for num in nums:
            digit = num

            while digit:
                digit_sum += digit % 10
                digit //= 10

            if digit_sum in count:
                ans = max(ans, num + count[digit_sum])

            count[digit_sum] = max(count[digit_sum], num)
            digit_sum = 0

        return ans
