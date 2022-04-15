# https://leetcode-cn.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row, col, board, num):
            # 行是否有重复
            for i in range(9):
                if board[row][i] == num:
                    return False
                    # 列是否有重复
            for i in range(9):
                if board[i][col] == num:
                    return False
                    # 九宫格
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def backTracking(board):
            for i in range(len(board)):  # 遍历行
                for j in range(len(board[0])):  # 遍历列
                    if board[i][j] != '.':
                        continue
                    for num in range(1, 10):
                        if isValid(i, j, board, str(num)):
                            board[i][j] = str(num)
                            if backTracking(board):  # 如果都能遍历完，那么返回
                                return True
                            board[i][j] = '.'  # 如果不能填完，回溯
                    return False  # 遍历完9个数字，依然找不到满意的结果，返回False
            return True  # 行，列都能遍历完，证明可以填完，返回True

        backTracking(board)


