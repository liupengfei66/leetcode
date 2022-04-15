# https://leetcode-cn.com/problems/jump-game/
# 到每个位置都跳出最大的距离，看看最终能否覆盖到终点
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
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