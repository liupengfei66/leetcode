# https://leetcode-cn.com/problems/ones-and-zeroes/submissions/
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

# 这题还是01规划，因为选的是子集，子集才是物品，m和n相当于是两个背包，所以这是个2维背包
# 正规来说，这题应该是个3位数组，即dp[k][i][j]表示在前k个字符串中，有i个0，j个1的最大子集个数为dp[k][i][j]
# 其他都与1维的01背包一样，所以这题的优化dp就是2维数组dp[i][j]
# 也因此，在遍历时先遍历物品，再遍历背包，背包需要倒序，因为默认是用dp[k][i][j]覆盖了dp[k-1][i][j]
# max也很容易理解，就是选择第k个字符串和不选择，不选择，就是原来的dp[i][j]，选择了，就是+1
# 不选择也很容易理解，就是当前的dp[i][j]在不选择的时候已经可以得到满足
# 比如当前是dp[3][3]，但是下一个字符串全是1，那么当考虑下一个字符串时，就不能放入dp[3][3]，此时dp[3][3]=dp[3][3]
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for _str in strs:
            ones = _str.count('1')
            zeros = _str.count('0')

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]