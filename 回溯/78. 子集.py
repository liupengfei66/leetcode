# https://leetcode-cn.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backTracking(candidates, start):
            res.append(path[:])
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backTracking(candidates, i+1)
                path.pop()

        backTracking(nums, 0)
        return res