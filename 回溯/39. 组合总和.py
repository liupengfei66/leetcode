# https://leetcode-cn.com/problems/combination-sum/
# 本题跟77，216没有什么本质的区别
# 但是本题是可以重复选取的，因此要注意边界情况，例如输入里不能有0，否则就无限选取0了
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        # 排序，方便回溯时判断，超出target后直接返回
        candidates.sort()

        def backTracking(candidates, target, start):
            if target < 0 or len(res) >= 150:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # 剪枝，如果总和已经大于target，直接退出，不继续递归
                if target - candidates[i] < 0:
                    return

                path.append(candidates[i])
                target -= candidates[i]
                backTracking(candidates, target, i)
                target += candidates[i]
                path.pop()

        backTracking(candidates, target, 0)
        return res





