# https://leetcode-cn.com/problems/permutations-ii/
# 跟前面的做法差不多，就是多了一个used数组用来判断树枝间不用重复的位置
# 注意下面的used[i]=True和False分别也是模拟了回溯的过程
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backTracking(nums):
            repeat = set()
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in repeat:
                    continue
                if used[i]:
                    continue
                repeat.add(nums[i])
                used[i] = True
                path.append(nums[i])
                backTracking(nums)
                path.pop()
                used[i] = False

        backTracking(nums)
        return res

# 解法2：同时利用used数组去重
# 解法2比较难理解，就用解法1吧
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        nums.sort()

        def backTracking(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # if i > 0 and nums[i-1]==nums[i] and used[i-1]  - 树枝去重
                if i > 0 and nums[i-1]==nums[i] and not used[i-1]:  # 树层去重
                    continue
                path.append(nums[i])
                used[i] = True
                backTracking(nums, used)
                used[i] = False
                path.pop()

        backTracking(nums, used)
        return res

