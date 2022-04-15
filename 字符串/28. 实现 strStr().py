# https://leetcode-cn.com/problems/implement-strstr/
# 经典的KMP算法
class Solution:
    def getNext(self, p):
        next = [0] * len(p)
        next[0] = 0
        i = 0
        for j in range(1, len(p)):
            while i > 0 and p[i] != p[j]:
                i = next[i - 1]
            if p[i] == p[j]:
                i += 1
            next[j] = i
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        # 构造next数组
        next = self.getNext(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1
        return -1