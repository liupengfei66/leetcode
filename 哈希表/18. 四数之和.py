# https://leetcode-cn.com/problems/4sum/
# 双指针法，与15.三数之和思路一致，时间复杂度O(n*n*n)
# 先固定两个数，其他如5数之和，6数之和也都一样
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n_nums = len(nums)

        for i in range(n_nums):
            # 这里就不能再判断，因为target可以为负值，假如第一个为-5，target为-6
            # 只要后面的数字为[-1 0 0]即可
            # if nums[i] > target:
            #     break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n_nums):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n_nums - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left != right and nums[left] == nums[left + 1]:
                            left += 1
                        while left != right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
