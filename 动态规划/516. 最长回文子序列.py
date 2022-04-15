# https://leetcode-cn.com/problems/longest-palindromic-subsequence/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] - s在[i,j]范围内的回文子序列长度为dp[i][j]
        dp = [[0] * n for _ in range(n)]

        # 初始化，单个字符是回文，长度为1
        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 两边字符相同，长度+2，可以画一个图看一下i和j的遍历关系
                # 注意i是不断减小，j是不断增大，所以dp[i][j]的上一个状态是dp[i+1][j-1]
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # 加入s[i]的回文长度为dp[i][j-1]，加入s[j]的回文长度为dp[i+1][j]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][n - 1]
