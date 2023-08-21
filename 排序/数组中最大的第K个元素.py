# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 超高概率的面试题，因为这题实际考察了排序方法
import random
from typing import List
random.seed(1)
# 快速排序，时间复杂度O(n)，虽然递归调用最坏是O(n*n)，但是因为使用了随机选择pivot，
# 可以确保分区操作在平均情况下将数组分成两个近似相等的部分, 所以期望的时间复杂度是O(n)
# 快排是O(nlogn)，但这里是找最大的K个，不是完整的快排
# 使用快排方法对数组进行倒序排列，当pivot等于k时，找到需要的数
# 此时无需关心左右子数组是否有序
class Solution:
    def randomPartition(self, arr, left, right):
        rand_pivot = random.randint(left, right)
        arr[rand_pivot], arr[right] = arr[right], arr[rand_pivot]

        pos = left
        pivot = right
        for i in range(left, right):
            # 从大到小排序
            if arr[i] <= arr[pivot]:
                continue
            # pos指向的始终是满足条件的
            # 如果arr[left] > arr[pivot]，那么当前arr[left]满足条件，pos去下一个位置
            # 如果arr[left] <= arr[pivot]，那么就会在arr[i] > arr[pivot]时被换走
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
        arr[pos], arr[pivot] = arr[pivot], arr[pos]
        return pos

    def quickSort(self, arr, left, right, k):
        # 这里与快排不太一样，相等也还是要执行的
        # 对于排序来说，只剩1个数字可以不排了，但对于返回第K个大的数，还需要继续判断的
        if left <= right:
            pivot = self.randomPartition(arr, left, right)
            if pivot == k:
                return arr[pivot]
            elif pivot < k:
                return self.quickSort(arr, pivot + 1, right, k)
            else:
                return self.quickSort(arr, left, pivot - 1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums, 0, len(nums) - 1, k)

s = Solution()
res = s.findKthLargest([3,2,1,5,6,4], 1)
print(res)

# 堆排序，时间复杂度=O(n+klogn)
# 构建大根堆,O(n)，调整O(logn)，整体是O(n)
# 取出K个元素，k * O(logn)
# 构建大根堆，每次从堆顶取最大元素，取K次后，就是第K个大的值
class Solution:
    def adjust_heap(self, arr, n_arr, root):
        l_child = root * 2 + 1
        r_child = root * 2 + 2
        max_node = root
        if l_child < n_arr and arr[max_node] < arr[l_child]:
            max_node = l_child
        if r_child < n_arr and arr[max_node] < arr[r_child]:
            max_node = r_child
        if max_node != root:
            arr[max_node], arr[root] = arr[root], arr[max_node]
            self.adjust_heap(arr, n_arr, max_node)

    def build_max_heap(self, arr):
        last_root = (len(arr)-2)//2
        for i in range(last_root, -1, -1):
            self.adjust_heap(arr, len(arr), i)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.build_max_heap(nums)
        for i in range(len(nums)-1, len(nums)-1-k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjust_heap(nums, i, 0)
        return nums[len(nums)-k]