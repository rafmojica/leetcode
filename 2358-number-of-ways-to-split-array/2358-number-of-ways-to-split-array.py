class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # build left section on the fly
        # right section = sum(nums) - left section
        ans = left_section = 0
        sumNums = sum(nums) # O(n) time

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = sumNums - left_section

            if left_section >= right_section:
                ans += 1

        return ans
