# https://leetcode-cn.com/problems/perfect-squares/
# 数字可以无限使用=>完全背包，跟322.零钱兑换基本一个套路了
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n

        nums = [i*i for i in range(1, n+1) if i*i <= n]
        for num in nums:
            for j in range(num, n+1):
                dp[j] = min(dp[j], dp[j-num]+1)

        return dp[n]