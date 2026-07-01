class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # use a prefix sum 
        prefixSum = [0] * (len(nums) + 1)
        lastIndex = {}
        res = left = 0

        for right in range(len(nums)):
            prefixSum[right + 1] = prefixSum[right] + nums[right]

            if nums[right] in lastIndex:
                left = max(left, lastIndex[nums[right]] + 1)
            
            lastIndex[nums[right]] = right
            res = max(res, prefixSum[right + 1] - prefixSum[left])

        return res
        