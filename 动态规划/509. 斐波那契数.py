# https://leetcode-cn.com/problems/fibonacci-number/
# 解法1：递归，跟DP没啥关系
# 时间复杂度：O(2^n)
# 空间复杂度：O(n) 算上了编程语言中实现递归的系统栈所占空间
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# 解法2：dp
# 1. 确定dp[i]和i的含义
# 2. 确定递推公式，dp[i] = dp[i-1] + dp[i-2]
# 3. dp数组初始化，dp[0]=0. dp[1]=1
# 4. 确定遍历顺序，本题就是根据n从前往后遍历
# 5. 举例推导dp数组
# 时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]