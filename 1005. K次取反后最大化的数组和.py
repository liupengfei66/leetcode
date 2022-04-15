# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/
# 解法1：每次都修改最小的值，变为最大的值，修改K次
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)

# 解法2
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True) # 按绝对值从大到小排序
        # 逐个修改负值为正值，直到没有负值
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        # 如果所有都是正值了，但是k还有，那么修改最小的值为负值
        if k > 0 and k % 2:
            nums[-1] = - nums[-1]
        return sum(nums)
