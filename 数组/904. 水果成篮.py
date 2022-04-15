# https://leetcode-cn.com/problems/fruit-into-baskets/
# 滑动窗口法，时间复杂度O(n)，空间复杂度O(n)
# 这题可以想到用滑动窗口，但是数据结构用hashmap是很聪明的，这样在滑动窗口收口时，可以依次滑动过去
# 其实这题可以想到用hashmap，因为指定了是两个类型，并且从滑动窗口看，顺序也不是一定先出现哪个类型
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, res = 0, 0
        baskets = collections.Counter()
        for i, fruit in enumerate(fruits):
            baskets[fruit] += 1
            while len(baskets) > 2:
                baskets[fruits[start]] -= 1
                if baskets[fruits[start]] == 0:
                    del baskets[fruits[start]]
                start += 1
            res = max(res, i - start + 1)
        return res
