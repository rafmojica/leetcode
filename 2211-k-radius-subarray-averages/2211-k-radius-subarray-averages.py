class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        window_size = 2*k + 1
        n = len(nums)
        result = [-1] * len(nums)
        
        if window_size > n:
            return result

        window_sum = sum(nums[:window_size])
        result[k] = window_sum // window_size

        for i in range(window_size, n):
            window_sum += nums[i] - nums[i - window_size]
            result[i - k] = window_sum // window_size

        return result
