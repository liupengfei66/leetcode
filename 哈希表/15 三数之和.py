# https://leetcode-cn.com/problems/3sum/submissions/
# 双指针法，时间复杂度O(n*n)
# 思路确实挺巧妙的，先排序，然后固定一个数，然后从剩下的里面寻找另外两个数
# 去重的想法也比较巧
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n_nums = len(nums)
        nums.sort()

        for i in range(n_nums):
            # 因为已经排序过，如果从这里就>0，那么总和是不可能为0的
            if nums[i] > 0:
                break
            # 如果在位置1之后的两个数相等，那么就会是同样的结果， 因为left right都是一样的
            # 而如果是需要连着两个一样的数，那么在a-1位置已经考虑过了
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n_nums - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left+1]:
                        left += 1
                    while left != right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

# 错误写法，哈希表法
# 错在前两个数的和可能是一致的，从而hashmap的key被覆盖了
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         hashmap = collections.defaultdict(list)
#         n_nums = len(nums)
#         for i in range(n_nums - 1):
#             for j in range(i + 1, n_nums):
#                 target = 0 - (nums[i] + nums[j])
#                 hashmap[target] = [i, j]
#
#         res = []
#         for k, num in enumerate(nums):
#             if num in hashmap and k not in hashmap[num]:
#                 tmp = [nums[x] for x in hashmap[num]]
#                 tmp.append(num)
#                 tmp.sort()
#                 if tmp not in res:
#                     res.append(tmp)
#
#         return res
