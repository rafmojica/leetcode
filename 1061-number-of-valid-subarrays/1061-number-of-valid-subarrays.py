class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        # monotonic stack
        stack = []
        ans = 0

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                ans += i - stack[-1]
                stack.pop()
            
            stack.append(i)

        while stack:
            ans += len(nums) - stack[-1]
            stack.pop()

        return ans        
