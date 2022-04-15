# https://leetcode-cn.com/problems/palindrome-partitioning/
# 字符串切割问题可以是个回溯问题
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def isHuiwen(s):
            # 对于pthon，有种简单的写法，即s == s[::-1]
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
            return True
        def backTracking(s, start):
            if start >= len(s):
                res.append(path[:])
            for i in range(start, len(s)):
                curr_s = s[start:i+1]
                if not isHuiwen(curr_s):
                    continue
                path.append(curr_s)
                backTracking(s, i+1)
                path.pop()

        backTracking(s, 0)
        return res
