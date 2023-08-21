# https://leetcode-cn.com/problems/combination-sum-iv/
# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。
# 请你从 nums 中找出并返回总和为 target 的元素组合的个数。

# 完全背包+装满背包+排列问题，具体的在518已经分析过
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[j] - 总和为j的排列数为dp[j]
        dp = [1] + [0] * target
        for j in range(1, target+1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]

        return dp[target]