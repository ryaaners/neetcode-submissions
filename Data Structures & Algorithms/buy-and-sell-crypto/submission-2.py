class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      left, right = 0, 1
      mostprofit = 0

      while right < len(prices):
        if prices[left] <= prices[right]:
            currprofit = prices[right] - prices[left]
            mostprofit = max(mostprofit, currprofit)
        else:
            left = right
        right += 1
      return mostprofit