class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # store index of prices in stack
        # if prices[top of stack] is >= current price, pop stack and update values by subtracting.
        # keep appending index if elem is not greater than the next.

        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]

            stack.append(i)

        return prices
        