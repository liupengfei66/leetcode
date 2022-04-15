# https://leetcode-cn.com/problems/house-robber-ii/
# 与198.打家劫舍不同的是，这里是成环的
# 实际上，只需要考虑两种情况，
# 1. 考虑队首，不考虑队尾
# 2. 考虑队尾，不考虑队首
# 事实上，其他的情况都包含在这两种情况中，例如如果是第二个比第一个大，那么在第2种情况就会考虑到队尾，得到最大值
# 如果从倒数第二个开始，那么其实跟第1种情况是一样的，数组从哪里开始，并不会影响最终的大小，只要顺序保持一致
from typing import List
class Solution:
    def robDetail(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums)-1]

    def rob(self, nums: List[int]) -> int:
        n_rooms = len(nums)
        if n_rooms == 0:
            return 0
        if n_rooms == 1:
            return nums[0]
        if n_rooms == 2:
            return max(nums[0], nums[1])

        # 偷第一间，不偷最后一间
        res1 = self.robDetail(nums[:-1])
        # 不偷第一间
        res2 = self.robDetail(nums[1:])

        return max(res1, res2)