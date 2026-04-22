class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n # resulting array filled with 0s
        rightMax = -1

        # [2,4,5,3,1,2]
        # [4,5,3,1,2] ...

        for i in range(n - 1, -1, -1): # decrementing for loop
            res[i] = rightMax # change from right to left
            rightMax = max(arr[i], rightMax)
        return res