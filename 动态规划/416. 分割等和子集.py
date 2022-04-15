# https://leetcode-cn.com/problems/partition-equal-subset-sum/
# 时间复杂度是O(n^2)，空间复杂度是O(n)，因为dp是大数组
# 本题是典型的01背包问题，nums是不用排序的
# 遇到整不明白的，可以画一个矩阵图对着看看，横轴是背包，纵轴是物品
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2:
            return False
        target = _sum // 2
        # dp[j] - 背包容量为j时，凑成的子集总和为dp[j]
        dp = [0] * (target+1)
        for i in range(len(nums)):
            # 注意这里的条件，j >= nums[i]，背包容量至少要等于nums[i]，否则不用考虑nums[i]了
            # 分为nums[i]放入与不放入，取两者最大
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])

        return dp[target] == target
