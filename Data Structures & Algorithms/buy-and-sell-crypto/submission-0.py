class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = len(prices) - 1
        j = 0
        high = 0
        while i>=0:
            for j in range(i):
                if prices[i] - prices[j] > high:
                    high = prices[i] - prices[j]

            i-=1

       

        return high

