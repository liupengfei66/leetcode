# https://leetcode-cn.com/problems/remove-element/submissions/
# 使用快慢指针，时间复杂度O(n),空间复杂度O(1)
# 快指针负责遍历，慢指针负责指示当前需要插入的位置，堪称完美
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

# 暴力，找到一个就移动数组
# 时间复杂度O(n^2)，空间复杂度O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)
        while start < end:
            if nums[start] == val:
                for i in range(start, end-1):
                    nums[i] = nums[i+1]
                end -= 1
            else:
                start += 1
        nums = nums[0:end]
        return len(nums)

# 改进版，只需要遍历一次，计算每个元素需要移动的次数
# 时间复杂度O(n),空间复杂度O(1)
# 这种方法的复杂度跟快慢指针是一致的，但是没有快慢指针容易理解
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
            else:
                nums[i-k] = nums[i]
        return len(nums) - k
