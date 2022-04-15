# https://leetcode-cn.com/problems/integer-break/
# 1. 确定dp[i]的含义，dp[i]表示正整数i拆分成至少两个正整数的和之后，这些和的最大乘积
# 2. 确定递推公式，dp[i] = max{j*(i-j), j*dp[i-j]}
# 假设i首先拆分出j,那么剩下的部分就是i-j，此时有两种选择：
# 1）i-j不再拆分，dp[i]=i*(i-j)
# 2）i-j继续拆分，那么就是dp[i]=j*d[i-j]
# 显然，j可以从1到i-1，所以对每个i，需要遍历，计算最优拆分点。
# 3. dp数组初始化，dp[0][1]和dp[1][0]必然都是等于1的，因为从(0,0)到这两个点都只有1种方法
# 4. 确定遍历顺序，本题就是先遍历i,然后对每个i，遍历j
# 5. 举例推导dp数组
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

# 解法2：这题还有数学的解法，不过我觉得这个没啥意思，刷Leetcode不是为了弄数学的
# 也就是n尽可能除以3
# 当余数为2时，则保留
# 当余数为1时，退一个3，替换为2+2,因为2x2>1x3
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)