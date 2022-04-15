# https://leetcode-cn.com/problems/monotone-increasing-digits/
# 看出来了是从后开始两个比较，变成9，但依然还是没想到贪心方法
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))
        for i in range(len(n) - 1, 0, -1):
            if n[i - 1] > n[i]:
                n[i - 1] = str(int(n[i - 1]) - 1)
                n[i:] = '9' * (len(n) - i)
        return int("".join(n))


