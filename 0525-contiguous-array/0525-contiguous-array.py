class Solution:
    def findMaxLength(self, nums: List[int]) -> int: 
        freq = {}
        freq[0] = -1
        ans = count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in freq:
                ans = max(ans, i - freq[count])
            else:
                freq[count] = i

        return ans
        