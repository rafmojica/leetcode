class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if 2*k >= len(nums):
            return [-1] * len(nums)
        
        result = [-1] * len(nums)
        curr = 0
        currAvg = lambda x: x // (2*k + 1)
        for i in range(2*k + 1):
            curr += nums[i]
        
        center = k
        
        for i in range(2*k, len(nums)):
            result[center] = currAvg(curr)
            center += 1
            if i != len(nums) - 1:
                curr += nums[i + 1] - nums[i - 2*k]
            
        return result
        