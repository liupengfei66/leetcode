# https://leetcode-cn.com/problems/n-queens/
# 采用回溯解决问题，思路就是把棋盘的行看做一层，递归的一层一层的调用下去
# 最终能到达叶子结点的，就是合理结果
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def isValid(row, col, chessboard):
            # 行不用判断，for循环保证了已经
            # 列
            for i in range(len(chessboard)):
                if chessboard[i][col] == 'Q':
                    return False
            # 斜线 左上角
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 斜线，右上角
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # 其他两个位置的斜线不用检查，因为我们是从上到下遍历棋盘的
            # 所以只需要看前面就好
            return True

        def backTracking(n, row, chessboard):
            if row == n:
                res.append(["".join(path) for path in chessboard])
                return
            for col in range(n):
                if not isValid(row, col, chessboard):
                    continue
                chessboard[row][col] = 'Q'
                backTracking(n, row + 1, chessboard)
                chessboard[row][col] = '.'

        chessboard = [['.'] * n for _ in range(n)]
        backTracking(n, 0, chessboard)
        return res
