# https://leetcode-cn.com/problems/unique-paths/
# 1. 确定dp[i][j]的含义，dp[i][j]表示到(i,j)位置，有多少种方法
# 可见，一般dp[i]都是直接与目标联系的
# 2. 确定递推公式，dp[i][j] = dp[i-1][j] + dp[i][j-1]
# 到达(i,j)只有两种方法，要么从左边来，要么从上边来，所以到达(i,j)的方法和就是这两种的方法和
# 3. dp数组初始化，dp[0][1]和dp[1][0]必然都是等于1的，因为从(0,0)到这两个点都只有1种方法
# 4. 确定遍历顺序，本题就是根据n从(0,0)到(m-1,n-1)
# 5. 举例推导dp数组
# 时间复杂度O(m*n)，空间复杂度O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

# 解法2：这题用数学的方法确实也可以解
# 一定有m-1步是往下的，所以从(m+n-2)步中，挑出这m-1步，剩下的就是横向移动的
# 所以最终的可能性就是C_{m+n-2}^{m-1}