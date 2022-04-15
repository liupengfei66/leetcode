# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/
# 贪心
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr, res = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
                res = max(curr, res)
            else:
                curr = 1
        return res

# 解法2：动态规划
# 比300题简单，因为是要求连续，一旦中断，就从0开始
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # dp[j] - nums从0到j（包含j）连续子序列长度
        dp = [1] * n
        res = 1
        for j in range(1, n):
            if nums[j] > nums[j-1]:
                dp[j] = dp[j-1] + 1
            res = max(res, dp[j])
        return res