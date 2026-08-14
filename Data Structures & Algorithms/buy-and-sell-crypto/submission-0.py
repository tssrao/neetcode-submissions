class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Complexity: O(n); 
        # for every iteration, current value is selling price
        # buying price is min of all values identified yet
        # calculate the profit
        
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(max_profit, (i-min_price))
        return max_profit
