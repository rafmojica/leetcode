class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1. implement a binary search
        # 2. if our pointer is on the target, return index.
        # 3. if two pointers end up together, and the target hasn't been found, return index + 1

        l, r = 0, len(nums) - 1

        while l <= r: # 0, 3
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l
