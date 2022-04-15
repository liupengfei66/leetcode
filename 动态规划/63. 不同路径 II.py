# https://leetcode-cn.com/problems/unique-paths-ii/
# 有了62.不同路径，这题还是比较容易想到的
# 主要的难点在于第一行和第一列的处理，在障碍物之后的dp应该设置为0
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 第一行和第一列在障碍物之前的应该设置为1，障碍物之后的还是0
        # 其他行列依赖计算即可
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]