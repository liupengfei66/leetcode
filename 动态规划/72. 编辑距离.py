# https://leetcode-cn.com/problems/edit-distance/
# 这题在583的基础上，增加了增/删/改 3种操作
# 时间复杂度分析：状态数为O(n*m)，状态计算为O(1)，因此总的时间复杂度为O(n*m)。

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        if n1 * n2 == 0:
            return max(n1, n2)

        # dp[i][j] word1[0~i],word2[0~j]的编辑距离为dp[i][j]
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        # 初始化，因为是从1开始，所以0需要初始化
        # 如果一个单词是空，那么显然编辑距离等于另外一个单词长度
        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                # 考虑word1的第i个字符和word2的第j个字符有以下几种情况
                # 两个字符相等，不操作
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 两个字符不相等
                else:
                    # 最难理解的是上一步用哪个时候的状态，可以这么理解，dp[i-1][j-1]表示word1[0~i-1]与word2[0~j-1]已经一样，
                    # 那么当考虑dp[i][j]时，也就是考虑word1[i]和word2[j]这两个字符，那么就存在以下几种情况
                    # 删 - 删word1，假如知道word1[0~i-1]与word2[0~j]匹配，那么只需要删除word1[i]，即dp[i-1][j]+1
                    # 删 - 删word2，假如知道word1[0~i]与word2[0~j-1]匹配，也只需要删除word2[j]，即dp[i][j-1]+1
                    # 增 - word1增加一个，等于word2删除一个
                    # 增 - word2增加一个，等于word1删除一个
                    # 改 - 改word1和word2一样，因为word1[0~i-1]与word2[0~j-1]已经一样，修改word1[i]或word2[j]都可以，即dp[i-1][j-1]+1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[n1][n2]
