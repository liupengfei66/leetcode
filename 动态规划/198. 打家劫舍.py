# https://leetcode-cn.com/problems/house-robber/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 1:
            return nums[0]

        # dp[j] - 偷到第j个房屋时，最大的金额
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for j in range(2, len(nums)):
            # 如果不偷当前房屋，那最大就是前一个房屋时的金额
            # 如果偷当前房屋，那最大就是前2个，加上当前的金额
            dp[j] = max(dp[j - 1], dp[j - 2] + nums[j])
        return dp[len(nums) - 1]

