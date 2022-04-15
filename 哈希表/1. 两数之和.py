# https://leetcode-cn.com/problems/two-sum/
# 这是第一题
# 题目比较简单，说了一定有答案，并且答案唯一
# 那么我们只要记录下来需要的另一个值，然后如果有匹配上，就输出即可
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[target - num] = i

