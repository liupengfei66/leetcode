# https://leetcode-cn.com/problems/squares-of-a-sorted-array/
# 双指针，分别比较首尾的大小。时间复杂度=O(n)，空间复杂度=O(n)
# 这题是根据题目具体想出来的，因为题目的描述表明，原数组是两头大中间小，所以比较两端即可
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums)
        left, right, pos = 0, len(nums) - 1, len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                new_nums[pos] = nums[left] * nums[left]
                left += 1
            else:
                new_nums[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return new_nums

