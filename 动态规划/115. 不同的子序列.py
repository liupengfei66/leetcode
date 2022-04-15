# https://leetcode-cn.com/problems/distinct-subsequences/
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n_s = len(s)
        n_t = len(t)

        # dp[i][j]表示s[0:i-1]中t[0:j-1]出现的个数为dp[i][j]
        dp = [[0] * (n_t + 1) for _ in range(n_s + 1)]
        # 如果两个都是空串，那么可以认为是t可以出现在s中
        dp[0][0] = 1
        # 如果s为空，t不为空，则s的子序列中不可能出现t
        for i in range(1, n_t):
            dp[0][i] = 0
        # 如果s不为空，t为空，那删除s即可
        for i in range(1, n_s):
            dp[i][0] = 1

        for i in range(1, n_s + 1):
            for j in range(1, n_t + 1):
                if s[i - 1] == t[j - 1]:
                    # 如果两个字符相等了，可以选择使用当前的s[i-1]，也可以不使用
                    # 例如s=bagg  t=bag，那么对于s的最后一个g，可以用，也可以不用
                    # 用了就等于dp[i-1][j-1]，不用就等于dp[i-1][j]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n_s][n_t]

