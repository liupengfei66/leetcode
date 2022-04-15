# https://leetcode-cn.com/problems/combination-sum-ii/
# 本题与39的不同在于，首先 数组不可以重复选取，每个元素只能选1次
# 其次，在一个组合内，可以有重复元素出现，但在不同组合间，结果不能重复
# 因此，本题是属于树层间的去重，因为假设candidates=[1,1,2]，那么在candidates[1]可以的，在candidates[0]都已经考虑过了
# 所以candidates[1]是需要跳过的
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backTracking(candidates, target ,start):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # 本题不加这个条件，ac不了
                # 题目限定了每个数字都在[1,30]，否则这个条件不能加
                # 假如candidates=[-3,-2,-1] taget=-6
                if target - candidates[i] < 0:
                    return
                # 同一层去重
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                target -= candidates[i]
                backTracking(candidates, target, i+1)
                target += candidates[i]
                path.pop()

        backTracking(candidates, target, 0)
        return res

