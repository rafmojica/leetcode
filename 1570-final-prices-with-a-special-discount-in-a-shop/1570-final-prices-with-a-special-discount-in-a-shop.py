class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # worst case O(n^2) (no discounts)
        res = []

        for i in range(len(prices)):
            curr = prices[i]
            discounted = curr

            for j in range(i + 1, len(prices)):
                if prices[j] <= curr:
                    discounted = curr - prices[j]
                    break
                
            res.append(discounted)

        return res
        