class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1

        while l < r:
            length = r - l
            if height[l] > height[r]:
                ans = max(ans, length * height[r])
                r -= 1
            elif height[r] > height[l]:
                ans = max(ans, length * height[l])
                l += 1
            elif height[r] == height[l]:
                ans = max(ans, length * height[l])
                l += 1
                r -= 1

        return ans