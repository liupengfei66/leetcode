# https://leetcode-cn.com/problems/target-sum/
# dp[j]表示凑成j，有多少种表达方式，再一次展示了dp[j]一般就是目标
# 当nums[i]时，有两种情况：
# 1. 不选择nums[i]，此时dp[j]保持不变，继承当前情况，不更新，对应二维数组时i-1时的情况。也就是不考虑当前的nums[i]，已经可以凑成dp[j]的方法数。
# 2. 选择nums[i]，此时dp[j]=dp[j-nums[i]]，这个很好理解，放入nums[i]，并没有增加表达方式。为什么此时不是等于dp[j]?
#    因为最初的思想来源于二维数组，在二维数组的情况下，dp[i-1][j]就是没考虑nums[i]的情况，所以当你选择nums[i]时，肯定不能是dp[i-1][j]，而应该是dp[i-1][j-nums[i]]
# 所以最后dp[j]就是上面两种情况的和，即dp[j]+dp[j-nums[i]]
# 整个表达式拆成加和减两部分，这个想法比较巧妙
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # add+subtract=target   add-subtract=sum
        # => add = (target+sum)/2，因为nums是整数数组，所以add肯定也是整数
        # 本题就转化为求组成add的方法有几种
        _sum = sum(nums)
        if abs(target) > _sum:
            return 0
        bag_size = (_sum + target)
        if bag_size % 2:
            return 0
        bag_size = bag_size // 2

        # dp[j] - 凑成j，有dp[j]种方法
        dp = [1] + [0] * bag_size
        for i in range(len(nums)):
            for j in range(bag_size, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[bag_size]