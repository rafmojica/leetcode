class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        while True:
            total = startValue
            for i in range(len(nums)):
                total += nums[i]
                if total < 1:
                    startValue += 1
                    break
            if total >= 1:
                break
        
        return startValue
        