class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: # base case
            return 0

        left = answer = 0
        curr = 1
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1

            answer += right - left + 1 # update by length of window
        
        return answer
