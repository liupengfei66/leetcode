# https://leetcode-cn.com/problems/maximum-subarray/
# 如果序列和开始小于0了，就抛弃这个序列，从下一个位置开始
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, count = float('-inf'), 0
        for num in nums:
            count += num
            if count > res:
                res = count
            if count < 0:
                count = 0
        return res

# 解法2：DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # dp[j] - 到第j个位置的最大和为dp[j]
        dp = [0] * n
        dp[0], res = nums[0], nums[0]
        for j in range(1, n):
            # 对每个位置j，要么是取连续数组+nums[j]，要么是重新计算，取nums[j]
            dp[j] = max(dp[j-1]+nums[j], nums[j])
            res = max(res, dp[j])
        return res

