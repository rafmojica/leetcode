class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # prefix sum? 
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            
        summation = (len(nums) ** 2 + len(nums)) // 2
        
        return summation - total
        