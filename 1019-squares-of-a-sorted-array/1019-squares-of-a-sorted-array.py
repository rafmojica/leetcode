class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # treat negative numbers as positive, use two pointers to place larger values in new array.
        l, r = 0, len(nums) - 1
        result = [0] * len(nums)

        for i in range(len(result) - 1, -1, -1): # start at last elem, stop at -1 (after 0), decrement.
            if abs(nums[l]) > abs(nums[r]):
                result[i] = nums[l] ** 2
                l += 1
            else:
                result[i] = nums[r] ** 2
                r -= 1
        
        return result        
