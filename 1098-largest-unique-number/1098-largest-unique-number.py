class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = [-1] * (max(nums) + 1) # create placeholder array
        maxUnique = -1
        
        for num in nums:
            freq[num] += 1
            
        for i in range(len(freq)):
            if freq[i] == 0:
                maxUnique = max(maxUnique, i)
                
        return maxUnique
        