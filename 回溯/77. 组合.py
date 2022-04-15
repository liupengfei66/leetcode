# https://leetcode-cn.com/problems/combinations/
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        def backTracking(n, k, start):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i) # 处理结点
                backTracking(n, k, i+1) # 递归处理其叶子结点
                path.pop() # 回溯
        backTracking(n, k, 1)
        return res


# 添加剪枝策略，提高效率
# 如果剩余的元素，不足以构成K个，那么就没必要再继续处理了
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backTracking(n, k, start):
            if len(path) == k:
                res.append(path[:])
                return
            # 剪枝策略，如果剩下的元素全选也不满足k个，那就不用递归和遍历了
            for i in range(start, n-(k-len(path))+2):
                path.append(i)
                backTracking(n, k, i+1)
                path.pop()
        backTracking(n, k, 1)
        return res
