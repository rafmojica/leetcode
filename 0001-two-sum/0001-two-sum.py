class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, v in enumerate(nums):
            diff = target - v

            if diff in prevMap:
                res = [prevMap[diff], i]
                break
                
            prevMap[v] = i

        return res
