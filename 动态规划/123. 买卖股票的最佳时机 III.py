# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
# 记住dp[i][x]表示状态，而不是当天的操作
# 这题与121，122其实并没有太大区别，还是分状态的考虑
# 不同之处在于，交易2次从不持有到持有，依赖的是交易1次不持有状态
# 这题应该默认是允许「在同一天买入并且卖出」这一操作
# 那么如果题目不允许同一天买入并卖出，dp[0][2]该怎么理解呢？个人理解应该是从第3天才考虑dp[0][2]的状态
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        # 总共5种状态
        # 交易0次，收益始终是0
        # 交易1次，当前持有/不持有
        # 交易2次，当前持有/不持有
        dp = [[0, 0, 0, 0] for _ in range(n)]
        dp[0][0] -= prices[0]
        dp[0][2] -= prices[0]

        for i in range(1, n):
            # 交易1次，持有
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            # 交易1次，不持有
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            # 交易2次，持有，注意再次持有应该是在产生过1次交易，并且不持有的状态
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            # 交易2次，不持有
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])

        return dp[n-1][3]