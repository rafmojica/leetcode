class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # any number that is NOT mod 3 == 1 or -1 (which is 2)
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        
        return count