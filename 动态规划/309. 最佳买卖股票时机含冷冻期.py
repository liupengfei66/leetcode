# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 这题主要的是理清4种状态，以及之间的关系
# 定义状态是不用考虑顺序的，因为都是依赖昨天的状态
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 跟122，123，124不同，没有限制次数，只考虑是否持有就好
        n = len(prices)
        if n == 0:
            return 0
        # 4个状态，持有/不持有/冷冻
        # 为了保证冷冻状态，还有有一个当天卖出状态，否则不知道是否冷冻状态
        dp = [[0, 0, 0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            # 持有=max(昨天持有，昨天不持有+今天买入，昨天冷冻+今天买入)
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][2]-prices[i])
            # 不持有=max(昨天不持有，昨天冷冻)
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            # 冷冻=昨天卖出
            dp[i][2] = dp[i-1][3]
            # 今天卖出=昨天持有+今天卖出
            dp[i][3] = dp[i-1][0] + prices[i]

        return max(dp[n-1][1], dp[n-1][2], dp[n-1][3])

