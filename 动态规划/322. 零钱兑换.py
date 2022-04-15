# https://leetcode-cn.com/problems/coin-change/
# 完全背包（背包从小到大遍历）
# 求的是最小coin个数，不强调是组合或排序，所以先遍历物品还是先遍历背包都一样
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[j] - 凑成j至少需要dp[j]个硬币
        dp = [0] + [float('inf')] * amount

        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)

        return dp[amount] if dp[amount] != float('inf') else -1

# 先背包后物品的顺序如下，结果是一样的
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for j in range(amount+1):
            for i in range(len(coins)):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)

        return dp[amount] if dp[amount] != float('inf') else -1