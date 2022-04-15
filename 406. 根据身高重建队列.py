# https://leetcode-cn.com/problems/queue-reconstruction-by-height/
# 这题还是挺巧妙的，有难度
# 与135 分糖果类似，这里也是要满足2个条件，那么就要分开考虑
# people的元素为[h, k]，先考虑k显然没啥用，那么就先考虑h
# 如果按h倒序排列，然后逐个按照k的位置插入.
# 因为已经按倒序排列了，并且队列一定可以重建
# 那么对于每一个k，前面一定是已经有大于k个的数字存在了，所以直接插入到第k个位置一定是对的
# 而后面一定比前面小，所以对前面是没有影响的，在插入时不用考虑后面的元素
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
