# https://leetcode-cn.com/problems/number-of-islands/
# 岛屿问题，都是搜索问题
# 岛屿数量就是从每个为1的地方开始搜索，并对结果加1，搜索到的地方设置为2。
# 因此，1次搜索就找到1个岛屿
from typing import List

class Solution:
    def inArea(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def dfs(self, grid, r, c):
        if not self.inArea(grid, r, c):
            return
        if grid[r][c] != "1":
            return

        grid[r][c] = "2"
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        n_r = len(grid)
        res = 0
        if n_r == 0:
            return res
        n_c = len(grid[0])

        for i in range(n_r):
            for j in range(n_c):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)
        return res

s = Solution()
res = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(res)