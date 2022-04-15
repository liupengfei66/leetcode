# https://leetcode-cn.com/problems/combination-sum-iv/
# 完全背包+装满背包+排列问题，具体的在518已经分析过
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[j] - 总和为j的排列数为dp[j]
        dp = [1] + [0] * target
        for j in range(target+1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]

        return dp[target]