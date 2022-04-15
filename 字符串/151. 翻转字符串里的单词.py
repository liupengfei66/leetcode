# https://leetcode-cn.com/problems/reverse-words-in-a-string/
# 先去除首尾和中间多余的空格
# 然后先翻转整个字符串，再翻转每个单词
class Solution:
    def reverse(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverseWords(self, s: str) -> str:
        s = list(s.strip())
        # 移除多余空格
        slow = 0
        for fast in range(len(s)):
            if fast > 0 and s[fast] == s[fast - 1] and s[fast] == ' ':
                continue
            s[slow] = s[fast]
            slow += 1
        s = s[0:slow]
        # 整体翻转
        s = self.reverse(s)
        i, res = 0, ''
        # 每个单词翻转
        for j in range(len(s)):
            if j == len(s) - 1:
                res += "".join(self.reverse(s[i:j + 1]))
            elif s[j] == ' ':
                res += "".join(self.reverse(s[i:j])) + ' '
                i = j + 1
        return res


