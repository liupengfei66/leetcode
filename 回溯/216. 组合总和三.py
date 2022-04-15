# https://leetcode-cn.com/problems/combination-sum-iii/
# 这题与77基本一致, 当然，也可以继续进行剪枝优化，这里就没写
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backTracking(k, start, target):
            if target < 0:
                return
            if target == 0 and len(path)==k:
                res.append(path[:])
                return
            for i in range(start, 10):
                path.append(i)
                target -= i
                backTracking(k, i+1, target)
                target += i
                path.pop()
        backTracking(k, 1, n)
        return res