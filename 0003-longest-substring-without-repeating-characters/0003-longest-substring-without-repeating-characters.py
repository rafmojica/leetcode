from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window with hash map
        # keep increasing window until we reach a duplicate letter
        # resize window until duplicate is gone
        # record size of each iteration
        count = defaultdict(int)
        left = right = ans = 0

        while right < len(s):
            count[s[right]] += 1

            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
            
        return ans
        