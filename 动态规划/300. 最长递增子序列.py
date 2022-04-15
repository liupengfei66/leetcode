# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# 子序列问题也是DP的经典题目
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        res = 1
        # dp[i] - nums从0到i(包含i)的最大递增子序列长度
        dp = [1] * n
        # 对每一个位置都重新计算
        for i in range(1, n):
            for j in range(i):
                # nums[j] 表示nums从0到j(包含j)的最大递增子序列长度
                # 那么如果nums[i] > nums[j]，自然也就长度+1
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            # dp[i]不一定是最大，假如nums[i]比较小，那么dp[i]肯定也就比较小
            res = max(res, dp[i])

        return res


