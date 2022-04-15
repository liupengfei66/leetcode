# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
# 假设初始现金为0元，买入就是减少了现金，所以是减
# 卖出是增加现金，所以是加，如果低买高卖，就是赚钱，是正值
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[j] - 第j天能获取的最大收益，有两种状态，当天持有/不持有股票
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] -= prices[0]

        for i in range(1, len(prices)):
            # 当天持有 - 前一天持有/不持有
            # 只能交易一次，所以前一个不持有的状态，最大收益一定是0
            dp[i][0] = max(dp[i-1][0], -prices[i])
            # 当天不持有 - 前一天持有/不持有
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])

        # 股票一定是在不持有的情况下收益更大，所以不用考虑dp[n-1][0]
        return dp[len(prices)-1][1]