class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # build prefix sum
        # left section = prefix[i]
        # right section = prefix[-1] - left section
        prefix = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        for i in range(len(nums) - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - left_section

            if left_section >= right_section:
                ans += 1

        return ans
