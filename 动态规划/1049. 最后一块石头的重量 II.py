# https://leetcode-cn.com/problems/last-stone-weight-ii/
# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0


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
