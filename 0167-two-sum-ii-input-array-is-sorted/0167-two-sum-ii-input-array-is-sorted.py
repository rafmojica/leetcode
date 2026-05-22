class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            else:
                l += 1

        return [l + 1, r + 1]

        # [-1, 0, 2, 3, 4] target: 4
        # [1, 2, 3, 4] target: 4
