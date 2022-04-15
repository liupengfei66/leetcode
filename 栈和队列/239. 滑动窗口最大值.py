# https://leetcode-cn.com/problems/sliding-window-maximum/
# 单调队列的经典题目，这题还是官方题解讲解的更好
# 首先，队列满足条件i<j，nums[i] >= nums[j]
# 因为假设在窗口中i<j，如果nums[i]<nums[j]，那么i就不需要存在于队列中，只保存j即可
# 所以，如果新的元素k>j(队尾元素)，并且nums[k]>nums[j]，那么直接移除j，追加k即可
# 所以，滑动窗口的最大值始终都在队首位置，当移动窗口时，如果窗口移除的元素恰好也是最大元素，那么队列中队首的元素也相应的移除
# 时间复杂度O(n)，空间复杂度O(k)
class MonotonousQueue:
    def __init__(self):
        # 如果用list，pop(0)时，时间复杂度O(n)
        self.queue = collections.deque()

    def pop(self, max_value):
        if self.queue and max_value == self.queue[0]:
            self.queue.popleft()

    def front(self):
        if self.queue:
            return self.queue[0]

    def push(self, value):
        # 注意这不能是>=，否则如果出现相同元素，如[7,5,7,1]时，第2个7会把第一个7在队列里替换掉
        # 那么当窗口滑动时，第2个7就被当做第1个7给删除了
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = MonotonousQueue()
        for i in range(k):
            queue.push(nums[i])
        res.append(queue.front())

        for i in range(k, len(nums)):
            queue.pop(nums[i - k])
            queue.push(nums[i])
            res.append(queue.front())
        return res

# 解法2：优先队列
# 思路与单调队列一致，只是借用了python自带的api heapq来实现队列的排序
# 时间复杂度O(nlogn)，这是优先队列的复杂度
# 空间复杂度O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        # 存储元素下标，方便滑动窗口移动时，剔除最左边的元素
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans

