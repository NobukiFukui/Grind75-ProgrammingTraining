# 04_BestTimetoByandSellStock
Author: WaveAlchemist  
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# 1st
方針：
pricesの各要素についてi+1番目の要素~最後の要素との差分を取り，
最大値をmax_profitsに格納
最終的にmax_profitsの最大値を返す
結果：
Time Limit Exceeded
pricesがとても大きい配列の時にかなり時間を食ってしまう

```Python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profits = []
        if len(prices) <= 1:
            return 0
        for i in range(len(prices)-1):
            profits = [prices[j]-prices[i] for j in range(i+1,len(prices))]
            max_profits.append(max(profits))
        return max(max(max_profits),0)
```

# 2nd
方針：
解答も参考にし，なるべくforループを使わない方針
（1度でforループを終えるように）
min_priceを無限，max_profitを0にして
pricesを順に参照してこれらを更新する
結果：
成功

```Python
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
```

# 3rd
方針：
野田さんのコメントを参考にfloatを使わずに処理する
結果：
成功

```Python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
```