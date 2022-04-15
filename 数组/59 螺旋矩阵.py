# https://leetcode-cn.com/problems/spiral-matrix-ii/
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        k = 1

        while left <= right and up <= down:
            # 赋值最中间的元素
            if left == right and up == down:
                res[left][left] = k
                break
            # 先按行
            for i in range(left, right):
                res[up][i] = k
                k += 1
            # 再按列
            for i in range(up, down):
                res[i][right] = k
                k += 1
            # 逆序行
            for i in range(right, left, -1):
                res[down][i] = k
                k += 1
            # 逆序列
            for i in range(down, up, -1):
                res[i][left] = k
                k += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        return res

