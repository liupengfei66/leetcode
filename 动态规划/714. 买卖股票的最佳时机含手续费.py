# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res, min_price = 0, prices[0]
        for i in range(1, len(prices)):
            # 情况1：在最低点买入
            if prices[i] < min_price:
                min_price = prices[i]
            # 情况2：交易亏损，不卖
            elif prices[i]-min_price-fee < 0:
                continue
            # 情况3：交易可以获利，更新最大卖出日期
            else:
                res += prices[i] - min_price - fee
                min_price = prices[i] - fee # 这一步很关键，因为要持续计算最大获利，第一步res+=已经计算了截止目前为止的获利总额，从下一步开始计算新的获利总额，此时最小买入点需要减去手续费，因为如果不是在当前步卖出，那么我们的总额应该是多一个手续费的，所以要把手续费加回来。也就是说，后面的最小买入点，至少要比当前买入点低1个手续费钱，否则的话，就是继续持有划算。
        return res

# 解法2：动态规划
# 其他与122题一样，这里要注意的就是理论上来说，手里持有股票肯定不可能有卖了获得收益多
# 但是因为这里有手续费，所以当手里的价值低于手续费时，就不如拿在手里
# 既然一笔交易一定要有手续费，所以我们可以把他在买入时收取，这样就保证最后一定时不持有股票收益是最高的
# 如果在卖出时计算手续费，最后需要return max(dp[n_prices-1][0], dp[n_prices-1][1])
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n_prices = len(prices)
        if n_prices == 0:
            return 0
        # dp[i][x]第i天 持有/不持有 股票能获得的最大收益
        dp = [[0, 0] for _ in range(n_prices)]
        dp[0][0] = -prices[0] - fee
        for i in range(1, n_prices):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[n_prices-1][1]