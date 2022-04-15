# https://leetcode-cn.com/problems/delete-operation-for-two-strings/
# 这题其实与1143，1135，392都一样，可以采用直接求最长公共子序列，然后总长度-最长公共子序列的方法
# 也可以按下面这样，每次字符不相同时，选择一个字符删除，或者两个都删除
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        # dp[i][j] - word1[0:i]与word2[0:j]相同所需的最小步数
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 可以不考虑dp[i-1][j-1]吧，因为dp[i-1][j], dp[i][j-1]一定是覆盖了dp[i-1][j-1]的
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[n1][n2]
