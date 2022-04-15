# https://leetcode-cn.com/problems/increasing-subsequences/
# 本质上，这题与40，90一样，只是这里没办法排序，所以使用了集合来避免同一层的重复
# 这里体现的更明显一些，一个backTracking函数内，都是同层
# 同树枝只有通过传入的两个参数nums和start来体现
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backTracking(nums, start):
            if len(path) >= 2:
                res.append(path[:])
            # 每一层都有一个自己的repeat集合
            # 因为repeat是作用于树层，所以不存在回溯问题
            repeat = set()
            for i in range(start, len(nums)):
                if len(path) > 0 and nums[i] < path[-1] or nums[i] in repeat:
                    continue
                path.append(nums[i])
                repeat.add(nums[i])
                backTracking(nums, i+1)
                path.pop()

        backTracking(nums, 0)
        return res