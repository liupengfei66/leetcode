# https://leetcode-cn.com/problems/subsets-ii/
# 这题跟40题一样
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backTracking(nums, start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backTracking(nums, i+1)
                path.pop()

        nums.sort()
        backTracking(nums, 0)
        return res