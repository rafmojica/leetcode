class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers data structure
        # if l + r < target, l += 1
        # if l + r > target, r -= 1
        l, r = 0, len(numbers) - 1

        while (numbers[l] + numbers[r] != target):
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1

        return [l + 1, r + 1]
