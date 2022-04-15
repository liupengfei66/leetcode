# https://leetcode-cn.com/problems/permutations/
# 这题是排列问题，与组合的区别在于，排列的树枝之间只要不用同一个就行，都是从0开始的
# 所以这里用了一个used数组，用来记录，树枝里用了哪些值
# 这里也可以看出，树枝之间，就要通过参数传递才行，树枝间的回溯，重用了used数组
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backTracking(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backTracking(nums, used)
                used[i] = False
                path.pop()

        backTracking(nums, used)
        return res