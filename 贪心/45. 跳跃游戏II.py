# https://leetcode-cn.com/problems/jump-game-ii/
# 每次都跳出最大距离，并且在最大距离内，找出下一跳最大的更新距离，直到覆盖终点。
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cover, curr, res, max_cover = 0, 0, 0, 0
        while curr <= cover:
            max_cover = max(nums[curr]+curr, max_cover)
            if curr == cover:
                cover = max_cover
                res += 1
            if cover >= len(nums)-1:
                return res
            curr += 1