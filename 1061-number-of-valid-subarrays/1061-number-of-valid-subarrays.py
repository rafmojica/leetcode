class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        # monotonic stack (hardest question i've done so far. how does one come up with this algorithm...)
        
        stack = []
        ans = 0

        for i, num in enumerate(nums):
            # calculate for subarrays with the largest elements in nums 
            while stack and nums[stack[-1]] > num:
                ans += i - stack[-1]
                stack.pop()
            
            stack.append(i)

        # stack now contains indices to elements in nums that are non-decreasing
        while stack:
            ans += len(nums) - stack[-1] # calculate remaining subarrays by subtracting len(nums) from the largest element first.
            stack.pop() # remove largest element from the right

        return ans
