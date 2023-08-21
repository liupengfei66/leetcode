# https://leetcode-cn.com/problems/perfect-squares/
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4

# 数字可以无限使用=>完全背包，跟322.零钱兑换基本一个套路了
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n

        nums = [i*i for i in range(1, n+1) if i*i <= n]
        for num in nums:
            for j in range(num, n+1):
                dp[j] = min(dp[j], dp[j-num]+1)

        return dp[n]