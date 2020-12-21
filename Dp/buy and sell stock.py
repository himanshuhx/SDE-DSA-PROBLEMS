# brute force 0(n^2) time 0(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        for i in range(n):
            for j in range(i,n):
                maxprofit = max(maxprofit, prices[j]-prices[i])
        return maxprofit

# single pass soln 0(n) time 0(1) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        maxprofit = 0
        minele = prices[0]
        for i in range(n):
            minele = min(minele, prices[i])
            maxprofit = max(maxprofit, prices[i] - minele)

        return maxprofit