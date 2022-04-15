# https://leetcode-cn.com/problems/find-common-characters/
# 这题倒没有想象中的简单

# 解法1：利用哈希表
# 对每个单词，取哈希表中的最小值，即获得最低出现的次数
import collections
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        word1_cnt = [0] * 26
        for char in words[0]:
            word1_cnt[ord(char) - ord('a')] += 1

        for i in range(1, len(words)):
            word_cnt = [0] * 26
            for char in words[i]:
                word_cnt[ord(char) - ord('a')] += 1
            for j in range(26):
                word1_cnt[j] = min(word1_cnt[j], word_cnt[j])

        for i in range(26):
            while word1_cnt[i] != 0:
                res.extend(chr(i + ord('a')))
                word1_cnt[i] -= 1
        return res

# 解法2：利用collections.Counter()
# 思路与解法1是一样的，只是换用collections.Counter()，可以显著减少代码量，提高可阅读性
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        if len(words) == 0:
            return res
        common = collections.Counter(words[0])
        for i in range(1, len(words)):
            common &= collections.Counter(words[i])

        for key, value in common.items():
            for _ in range(value, 0, -1):
                res.append(key)
        return res

