# https://leetcode-cn.com/problems/is-subsequence/
# 实际上，这题与1143和1135是一样的，都是求最长公共子序列问题
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        if ns == 0:
            return True
        # dp[i][j] - s[0-i]和t[0-j]的子序列长度，不包含i和j
        dp = [[0] * (nt + 1) for _ in range(ns + 1)]
        for i in range(1, ns + 1):
            for j in range(1, nt + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        if dp[ns][nt] == ns:
            return True
        else:
            return False