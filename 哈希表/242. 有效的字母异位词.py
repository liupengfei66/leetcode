# https://leetcode-cn.com/problems/valid-anagram/
# 解法1
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = collections.Counter(s)
        c_t = collections.Counter(t)
        return c_s == c_t

# 解法2：可以利用defaultDict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for x in s:
            s_dict[x] += 1

        for x in t:
            t_dict[x] += 1

        return s_dict == t_dict

# 解法3：数组
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord("a")] += 1

        for i in range(len(t)):
            record[ord(t[i]) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                # record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True
