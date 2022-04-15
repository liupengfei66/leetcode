# https://leetcode-cn.com/problems/climbing-stairs/submissions/
# 这题跟377是完全一样的
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[j] - 到达j层台阶，有dp[j]种方法
        dp = [1] + [0] * n
        nums = [1, 2]
        for j in range(n + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]

        return dp[n]


# 空间复杂度是可以优化的，但还是上面的方法更能体现思想
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b, c = 1, 2, 0
        for i in range(3, n+1):
            c = a + b
            a, b = b, c
        return c

# 解法2：这题也可以用回溯解决
# 但是当n太大后，可能会超时
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        res = 0
        def backTracking(n, total):
            if total > n:
                return
            if total == n:
                nonlocal res
                res += 1
                return
            for i in range(1, 3):
                total += i
                backTracking(n, total)
                total -= i

        backTracking(n, 0)
        return res
s = Solution()
print(s.climbStairs(3))