class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # best case: O(n^2) time
        # sort nums: O(nlogn) time
        # using two pointers:
        #   - save the leftmost value (a) in sorted array
        #   - use two pointers such that left is in position (a+1) and right is len(nums) - 1
        #   - save all three values in a sum variable. using sum:
        #       - if > 0, decrement right pointer
        #       - if < 0, increment left pointer
        #       - if l == r, increment a and reset l and r pointers.
        
        # [-4, -1, -1, 0, 1, 2]

        nums.sort()
        res = []

        # [-1, -1, -1, 0, 0, 1, 1]

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]: # skip duplicate values if any (for v)
                continue

            l, r = i + 1, len(nums) - 1

            while r > l:
                currSum = v + nums[l] + nums[r]

                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1 # if we encounter THE SAME l value again, skip that.

        return res
