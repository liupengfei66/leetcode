# https://leetcode-cn.com/problems/longest-common-subsequence/
# 这题与718很像，只是序列不再连续,
# 分析这个的递推公式，就是假设text1[0:i-1]与text2[0:j-1]相同，那么此时考虑text1[i]与text[j]怎么办？
# 显然，他俩相等，dp[i][j]=dp[i-1][j-1]+1，不相等则取上一步中较长的。
# 718在nums1[i]!=nums2[j]的情况下，dp[i][j]=0，所以不用考虑前面状态
# 在两个数组的情况下，转移应该是涉及4个状态的，有dp[i][j-1],dp[i-1][j],dp[i-1][j-1],dp[i][j]
# 所以相等时考虑dp[i-1][j-1]->dp[i][j]，不相等时考虑dp[i][j-1],dp[i-1][j]->dp[i][j]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        if n1 == 0 or n2 == 0:
            return 0
        # dp[i][j] - text1[0:i]和text2[0:j]的公共子序列长度，不包含i和j
        # 这么做是为了保证代码一致性
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                # 相同，长度+1，这没毛病，关键是不相同时怎么办
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # 当两个不同时，取当前最大的长度继承下来
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n1][n2]
