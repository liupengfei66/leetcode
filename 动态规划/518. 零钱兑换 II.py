# https://leetcode-cn.com/problems/coin-change-2/
# 完全背包的背包就是从小到大遍历，想不明白，可以按第一个例子手动画一下就明白了
# 这题跟494是一个性质的，属于背包装满问题
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[j] - 凑成j的组合数为dp[j]，初始化dp[0]=1，为了递推公式，可以理解为凑成0块钱有1种方案，就是不取
        dp = [1] + [0] * amount
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]

        return dp[amount]