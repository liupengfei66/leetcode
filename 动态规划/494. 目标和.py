# https://leetcode-cn.com/problems/target-sum/
# 给你一个非负整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。


# dp[j]表示凑成j，有多少种表达方式，再一次展示了dp[j]一般就是目标
# 当nums[i]时，有两种情况：
# 1. 不选择nums[i]，此时dp[j]保持不变，继承当前情况，不更新，对应二维数组时i-1时的情况。也就是不考虑当前的nums[i]，已经可以凑成dp[j]的方法数。
# 2. 选择nums[i]，此时dp[j]=dp[j-nums[i]]，这个很好理解，在已经选择nums[i]的情况下，即应该有dp[j-nums[i]]种方法，
# 例如dp[j]，j为5，已经有一个1（nums[i]） 的话，有 dp[4]种方法 凑成 容量为5的背包。
# 所以最终的方法数，就是这两种情况的和，即dp[j] + dp[j-nums[i]]
# 初始值dp[0]=1，否则后面的递推都是0了。考虑nums: [1, 1, 1, 1, 1], d[1] += dp[0]，如果dp[0]=0，那么dp[1]=0 => dp[j]=0

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # add+subtract=target   add-subtract=sum
        # => add = (target+sum)/2，因为nums是整数数组，所以add肯定也是整数
        # 本题就转化为求组成add的方法有几种
        _sum = sum(nums)
        if abs(target) > _sum:
            return 0
        bag_size = (_sum + target)
        if bag_size % 2:
            return 0
        bag_size = bag_size // 2

        # dp[j] - 凑成j，有dp[j]种方法
        dp = [1] + [0] * bag_size
        for i in range(len(nums)):
            for j in range(bag_size, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[bag_size]
    

# 回溯法
class Solution:
    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path[:])  # 将当前路径的副本添加到结果中
        # 如果 sum + candidates[i] > target，则停止遍历
        for i in range(startIndex, len(candidates)):
            if total + candidates[i] > target:
                break
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i + 1, path, result)
            total -= candidates[i]
            path.pop()

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total:
            return 0  # 此时没有方案
        if (target + total) % 2 != 0:
            return 0  # 此时没有方案，两个整数相加时要注意数值溢出的问题
        bagSize = (target + total) // 2  # 转化为组合总和问题，bagSize就是目标和

        # 以下是回溯法代码
        result = []
        nums.sort()  # 需要对nums进行排序
        self.backtracking(nums, bagSize, 0, 0, [], result)
        return len(result)
