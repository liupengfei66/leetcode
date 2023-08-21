# https://leetcode-cn.com/problems/coin-change/
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。

# 完全背包（背包从小到大遍历）
# 求的是最小coin个数，不强调是组合或排序，所以先遍历物品还是先遍历背包都一样
# 凑足总金额为0所需的硬币个数肯定是0，所以dp[0]=0
# 考虑到递推公式的特性，dp[j]必须初始化为一个最大的数，否则就会在min(dp[j - coins[i]] + 1, dp[j])比较的过程中被初始值覆盖。
# 推导过程 coins = [1, 2, 5], amount = 5为例
# amount 0 1 2 3 4 5
# coin=1 0 1 2 3 4 5
# coin=2 0 1 1 2 2 3
# coin=5 0 1 1 2 2 1


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