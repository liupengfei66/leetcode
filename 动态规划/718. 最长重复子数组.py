# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
# 分析这个的递推公式，就是假设nums1[0:i-1]与nums2[0:j-1]相同，那么此时考虑nums1[i]与nums[j]怎么办？
# 显然，他俩相等，dp[i][j]=dp[i-1][j-1]+1，不相等则为0
from typing import List
# 解法一：暴力，时间复杂度O(n*n*n)
# 挨个比较nums1和nums2，遇到相等的就在此位置开始计算重复子数组个数
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            for j in range(n2):
                k = 0
                while k < min(n1 - i, n2 - j) and nums1[i + k] == nums2[j + k]:
                    k += 1
                res = max(res, k)

        return res

# 动态规划法，暴力法每个i和j，都要重新开始遍历完剩下的数组，我们希望只比较一次就行
# 时间复杂度O(M*N)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1) + 1  # 从递推公式可以看出，需要从1开始，所以这里加一，方便写代码
        n2 = len(nums2) + 1
        if n1 == 1 or n2 == 1:
            return 0
        res = 0
        # dp[i][j] - nums1中以i结尾和nums2中以j结尾的公共子数组长度为dp[i][j]
        # 因为每次比较的是nums1[i]和nums2[j]，所以dp[i][j]必然由dp[i-1][j-1]推导而来
        # dp[i][j] i维度是外层，j维度是内层
        dp = [[0] * n2 for _ in range(n1)]
        for i in range(1, n1):
            for j in range(1, n2):
                # 公共子数组是连续的，所以相等就是在dp[i-1][j-1]的基础上+1，dp[i-1][j-1]表示nums1[0:i-1]与nums2[0:j-1]有dp[i-1][j-1]个连续重复子数组
                # 不相等就直接归0，而因为初始化是0，所以就没有再单独处理
                # 可以对比1143，1143就是不连续的情况，718的情况就需要记录下最长长度，因为可能出现在中间
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
        return res

# 滑动窗口法，相当于是将嵌套循环拆成了2个单独的循环
# 每个都采用移动窗口的办法，如果有重复子数组，肯定有一个位置重复子数组是能对齐的。
# 例如 A=[5,6,2,8], B=[1,2,3,4]，当B不动，A左移一个位置时=[6,2,8]，此时与B按同等位置比较，则从第2个位置开始，就出现了相同的元素
class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def findMaxLen(addA, addB, length):
            max_len = k = 0
            for i in range(length):
                if nums1[addA + i] == nums2[addB + i]:
                    k += 1
                else:
                    k = 0
                max_len = max(max_len, k)
            return max_len

        res = 0
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            res = max(res, findMaxLen(i, 0, min(n1 - i, n2)))

        for i in range(n2):
            res = max(res, findMaxLen(0, i, min(n1, n2 - i)))

        return res

