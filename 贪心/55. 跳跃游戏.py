# https://leetcode-cn.com/problems/jump-game/
# 给定一个非负整数数组nums, 你最初位于数组的第一个下标.
# 数组中的每个元素代表你在该位置可以跳跃的最大长度,判断你是否能够到达最后一个下标。
# eg: nums = [2,3,1,1,4], 0>1, 1->3, 3->最后。
# 核心思想：如果一个位置能够到达，那么这个位置左侧所有位置都能到达。
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        # cover - 当前能够到达的最远位置
        # i 当前位置，每次往右跳一格，然后更新cover能达到的最大位置
        cover, i = 0, 0
        while i <= cover:
            cover = max(nums[i]+i, cover)
            if cover >= len(nums)-1:
                return True
            i += 1
        return False

# 解法2：提供一个我自己一开始的思路吧
# 不存在跳不过去的，就是可以跳过去
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        for i in range(len(nums)):
            if nums[i] == 0:
                flag = True
                for j in range(0, i):
                    if nums[j] > i-j or (nums[j] >= i-j and i == len(nums)-1):
                        flag = False
                        break
                if flag:
                    return False
        return True