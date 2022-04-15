# https://leetcode-cn.com/problems/last-stone-weight-ii/
# 本题可以转化为01背包问题，与416思路一致
# 从题目描述来看，显然，如果能分成重量均匀的两堆石头，那么最终就会得到最小的差值
# 所以本题就转换为了如何获得1/2重量的石头，类似于416. 分割等和子集
# _sum-target是_sum中target剩余的部分，因为是_sum//2，所以_sum-target>=target
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) <= 0:
            return 0
        _sum = sum(stones)
        target = _sum // 2

        # dp[j] - 背包容量为j时，石头的最大重量为dp[j]
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])

        return _sum - dp[target] - dp[target]
