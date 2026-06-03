class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for right in range(k):
            curr += nums[right]
            
        ans = curr
            
        for right in range(k, len(nums)):
            curr += nums[right] - nums[right - k]
            ans = max(ans, curr)
            
        return ans / k
    