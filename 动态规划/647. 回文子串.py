# https://leetcode-cn.com/problems/palindromic-substrings/
# 这题的dp[i][j]设置的比较秀，靠自己很难想到
# 时间复杂度=空间复杂度=O(n*n)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        # dp[i][j] - s[i:j]是否回文子串，s[i:j]左闭右闭
        # 状态转移公式的推导方法为，如果s[i]!=s[j]，那当前自然不是回文，res不增加
        # 如果s[i] == s[j]，分几种情况：
        # 1. j-i <= 1, 那么自然是回文
        # 2. j-i >= 2 ，就等于dp[i+1][j-1]
        # 根据状态转移公式，所以i需要从大到小遍历，j需要从小到大遍历
        dp = [[False]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        res += 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1
        return res

# 双指针法
# 这题也可以采用双指针法，对每个位置进行判断，分为单字母作为中心点和双字母作为中心点
# 时间复杂度=O(n*n)，空间复杂度=O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        def countString(i, j, n):
            res = 0
            while i >= 0 and j < n and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res

        res = 0
        for i in range(len(s)):
            # 以i为中心
            res += countString(i, i, len(s))
            # 以i和i+1为中心
            res += countString(i, i + 1, len(s))
        return res



