# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/
# 这题的思路与123. 买卖股票的最佳时机III是一样的，只是换成了可以交易K次
# 所以遵循上一题的思路即可，每个状态都是依赖前一个状态
# 0状态是没操作，为了交易1次时的持有状态保持一致，所以引入0状态。
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        # n_status=0表示不交易，其他情况，奇数是持有，偶数是不持有
        n_status = 2 * k + 1
        dp = [[0] * n_status for _ in range(n)]
        for i in range(1, n_status, 2):
            dp[0][i] = -prices[0]

        for i in range(1, n):
            for j in range(1, n_status):
                # 奇数，表示当前持有状态，由上一个持有状态和上一次交易的不持有状态得到
                if j % 2:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])

        return dp[n - 1][n_status - 1]
