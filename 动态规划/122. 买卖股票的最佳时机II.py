# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
# 这题其实可以观察到prices[3]-prices[1]=(prices[3]-prices[2])+(prices[2]-prices[1])
# 也就是说，如果你1天买入，第3天卖出，等价于第1天买入，第2天卖出，第三天再买入，第3天卖出
# 那么，收益最高的，一定就是在相隔两天是正收益的时间买卖
# 设想，如果中间几天是负收益的话，那肯定不如最后一个是正收益的，因为前面加入了负值，降低了总收益
# 同时，是否存在前面几天有正有负，但加起来是正的呢？那也不如，就取那天是正的
# 只取正的收益，相当于是说，天是我们操作的最小单位，我们选择只在赚钱的两天之间操作，那显然收益应该是最大的
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            res += max(prices[i+1] - prices[i], 0)

        return res


# 解法2：动态规划
# 假设初始现金为0元，买入就是减少了现金，所以是减
# 卖出是增加现金，所以是加，如果低买高卖，就是赚钱，是正值
# 这题与121基本一致，区别在于这里可以多次交易
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0] - 第i天持有股票获取的最大收益为dp[i][0]，dp[i][1] - 第i天不持有股票
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            # 当天持有，因为可以多次交易，所以=前一天持有+保持 或者 前一天不持有+买入
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            # 当天不持有=前一天持有+卖出 或者 前一天不持有+保持
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])

        # 股票一定是在不持有的情况下收益更大，所以不用考虑dp[n-1][0]
        return dp[n-1][1]