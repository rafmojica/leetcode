class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        output = 0
        for x in arr:
            if x + 1 in seen:
                output += 1

        return output
        