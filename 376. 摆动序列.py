# https://leetcode-cn.com/problems/wiggle-subsequence/
# 这题还是蛮精巧的，如果按照高低把图画出来，可能还容易想出贪心的方法
# 否则很难想到贪心
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre_diff, curr_diff, res = 0, 0, 1
        for i in range(len(nums)-1):
            curr_diff = nums[i+1] - nums[i]
            if curr_diff != 0 and curr_diff * pre_diff <= 0:
                res += 1
                pre_diff = curr_diff
        return res
