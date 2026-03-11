class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        # set l to r if (r < l), because we want to buy the cheapest stock
        # l dictates when we're buying
        # r dictates when we're selling
        l, r = 0, 1
        currMax = 0
        while r < len(prices):
            currMax = max(currMax, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return currMax