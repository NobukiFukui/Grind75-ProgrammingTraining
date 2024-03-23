# ===============================================================
# (program) 04_Best Time to Buy and Sell Stock
# WaveAlchemist
# # Description: 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# ===============================================================

# %% 1st
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         max_profits = []
#         if len(prices) <= 1:
#             return 0
#         for i in range(len(prices)-1):
#             profits = [prices[j]-prices[i] for j in range(i+1,len(prices))]
#             max_profits.append(max(profits))
#         return max(max(max_profits),0)



# prices = [7,1,5,3,6,4]
# Solution.maxProfit([],prices)

# %% 2nd

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


prices = [7,1,5,3,6,4]
Solution.maxProfit([],prices)
# %%
