class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create empty hashmap
        # O(n)
        prevMap = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[nums[i]] = i
        return []
        