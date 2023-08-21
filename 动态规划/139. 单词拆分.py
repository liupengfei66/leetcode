# https://leetcode-cn.com/problems/word-break/
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

# 这题可以想到用完全背包，但是怎么用还是一个问题
# 这题确实是先遍历背包更方便一些
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[j] - s[0:j]是可以被拆分的
        dp = [True] + [False] * len(s)

        for j in range(len(s) + 1):
            for i in range(0, j):
                # s[i:j] 中的每个子串，是否可以拆分
                curr = s[i: j]
                # 如果当前子串可拆分，并且除去该子串依然可拆分，则dp[j]可拆分
                if curr in wordDict and dp[j - (j - i)]:
                    dp[j] = True

        return dp[len(s)]
