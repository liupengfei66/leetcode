# https://leetcode-cn.com/problems/min-cost-climbing-stairs/
# 1. 确定dp[i]和i的含义，dp[i]表示到达第一个台阶，需要花费的体力
# 2. 确定递推公式，dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
# 因为第i个台阶，总可以假设从第i-1台阶爬1个台阶或第i-2个台阶爬2个台阶，但都必须支付所需的体力
# 3. dp数组初始化，dp[0]=0. dp[1]=0. 初始是假设还没开始爬
# 4. 确定遍历顺序，本题就是根据n从前往后遍历最终到达n才是登顶
# 5. 举例推导dp数组
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]


