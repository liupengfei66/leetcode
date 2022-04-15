# https://leetcode-cn.com/problems/candy/
# 分开考虑左右两边
# 要同时满足左右两边的条件，所以取max
class Solution:
    def candy(self, ratings) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)